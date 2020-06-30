from manimlib.imports import *

def curva_eliptica(self, t, n):
	if n:
		return self.coords_to_point(t, math.sqrt(t**3 - 2*t + 3))
	else:
		return self.coords_to_point(t, -math.sqrt(t**3 - 2*t + 3))

def posicion(self, t, func, letra, dir = UP):
	punto = Dot(
	           	self.input_to_graph_point(t,func)*RIGHT + self.input_to_graph_point(t,func)*UP)

	texto = TextMobject(letra).scale(3/4)
	texto.next_to(self.input_to_graph_point(t,func), dir)
	res = VGroup(punto, texto)
	return res

def recta(self, t1, t2, func1, func2):
	graph = ParametricFunction(
            lambda u: (1-u)*self.input_to_graph_point(t1, func1) + (u)*self.input_to_graph_point(t2, func2), 
            color = RED, t_min = 0, t_max = 1
            )
	return graph

class Asociatividad(GraphScene):
    def construct(self):

        ejes1 = Axes(
            x_min = -4, x_max = 4,
            y_min = -4, y_max = 4,
            #center_point = LEFT*3,
            x_axis_config = {
                "tick_frequency" : 1,
                "color" : BLUE,
                "unit_size": .7,
            },
            y_axis_config = {
                "tick_frequency" : 1,
                "color" : BLUE,
                "unit_size": .7,
            },
        )

        ejes2 = Axes(
            x_min = -4, x_max = 4,
            y_min = -4, y_max = 4,
            #center_point = RIGHT*3,
            x_axis_config = {
                "tick_frequency" : 1,
                "color" : BLUE,
                "unit_size": .7,
            },
            y_axis_config = {
                "tick_frequency" : 1,
                "color" : BLUE,
                "unit_size": .7,
            },
        )

       	graph11 = ParametricFunction( lambda t: curva_eliptica(ejes1, t, True),
       								color = GREEN,
                                    t_min = -1.8932891963044975,
                                    t_max = 2.7
                                    )

       	graph12 = ParametricFunction( lambda t: curva_eliptica(ejes1, t, False),
       								color = GREEN,
                                    t_min = -1.8932891963044975,
                                    t_max = 2.7
                                    )
       	
       	curva_eliptica1 = VGroup(graph11, graph12)

       	grafica1 = VGroup(ejes1, curva_eliptica1)

       	graph21 = ParametricFunction( lambda t: curva_eliptica(ejes2, t, True),
       								color = GREEN,
                                    t_min = -1.8932891963044975,
                                    t_max = 2.7
                                    )

       	graph22 = ParametricFunction( lambda t: curva_eliptica(ejes2, t, False),
       								color = GREEN,
                                    t_min = -1.8932891963044975,
                                    t_max = 2.7
                                    )
       	
       	curva_eliptica2 = VGroup(graph21, graph22)

       	grafica2 = VGroup(ejes2, curva_eliptica2)
       	
       	ecuacion = TextMobject("$y^2 = x^3 - 2x + 3$")
        ecuacion.to_edge(UP)

        todo = VGroup(grafica2, grafica1)

       	self.play(ShowCreation(todo,rate_func = slow_into, run_time = 3))
       	self.wait()
       	self.play(todo.arrange,LEFT)

       	self.play(
       	#	ShowCreation(ejes1, rate_func = exponential_decay, run_time = 3),
       	#	ShowCreation(ejes2, rate_func = exponential_decay, run_time = 3),
        #    ShowCreation(graph11, rate_func = slow_into, run_time = 2),
        #    ShowCreation(graph12, rate_func = slow_into, run_time = 2),
        #    ShowCreation(graph21, rate_func = slow_into, run_time = 2),
        #    ShowCreation(graph22, rate_func = slow_into, run_time = 2),
            ShowCreation(ecuacion),
        )

       	q = ["$C$", "$P$", "$Q$"]
       	p = [0, 1, 2]
       	r = zip(p, q)
       	s = zip(p,q)

        puntos1 = VGroup(*[posicion(ejes1, i[0], curva_eliptica1[0], i[1]) for i in r])
        puntos2 = VGroup(*[posicion(ejes2, i[0], curva_eliptica2[0], i[1]) for i in s])

        grafica1.add(puntos1)
        grafica2.add(puntos2)

        self.play(
        	ShowCreation(puntos1),
        	ShowCreation(puntos2),
        )

        recta1 = recta(ejes2, 2, 6-2*math.sqrt(14), graph21, graph22)

        puntos2.add(posicion(ejes2, 6-2*math.sqrt(14), curva_eliptica2[1], "$S1$"))

        self.play(
        	ShowCreation(recta1, rate_func = linear, run_time = 1),
        	ShowCreation(puntos2[len(puntos2)-1])
        )

        recta2 = recta(ejes2, 6-2*math.sqrt(14), 6-2*math.sqrt(14), graph22, graph21)
        
        puntos2.add(posicion(ejes2, 6-2*math.sqrt(14), curva_eliptica2[0], "$P+Q$"))
        
        self.play(
        	ShowCreation(recta2, rate_func = linear, run_time = 1),
        	ShowCreation(puntos2[len(puntos2)-1]),
        	FadeOut(recta1),
        	FadeOut(puntos2[len(puntos2)-2]),
        )

        recta3 = recta(ejes2, 6-2*math.sqrt(14), 1.486831897, graph21, graph21)

        puntos2.add(posicion(ejes2, 1.486831897, curva_eliptica2[0], "$S2$"))
        
        self.play(
        	ShowCreation(recta3, rate_func = linear, run_time = 1),
        	ShowCreation(puntos2[len(puntos2)-1]),
        	FadeOut(recta2),
        )

        recta4 = recta(ejes2, 1.486831897, 1.486831897, graph21, graph22)

        puntos2.add(posicion(ejes2, 1.486831897, curva_eliptica2[1], "$(P+Q)+C$", DOWN))
        
        self.play(
        	ShowCreation(recta4, rate_func = linear, run_time = 1),
        	ShowCreation(puntos2[len(puntos2)-1]),
        	FadeOut(recta3),
        	FadeOut(puntos2[len(puntos2)-2]),
        )

        Titulo1 = TextMobject("$(P+Q)+C$")
        Titulo1.to_corner(DOWN + RIGHT)

        self.play(
        	ShowCreation(Titulo1,run_time=3),
        	FadeOut(recta4),
        	)

        recta1 = recta(ejes1, 2, (1-math.sqrt(21))/2, graph11, graph11)

        puntos2.add(posicion(ejes1, (1-math.sqrt(21))/2, curva_eliptica1[0], "$R1$"))

        self.play(
        	ShowCreation(recta1, rate_func = linear, run_time = 1),
        	ShowCreation(puntos2[len(puntos2)-1])
        )

        recta2 = recta(ejes1, (1-math.sqrt(21))/2, (1-math.sqrt(21))/2, graph11, graph12)

        puntos2.add(posicion(ejes1, (1-math.sqrt(21))/2, curva_eliptica1[1], "$Q+C$"))

        self.play(
        	ShowCreation(recta2, rate_func = linear, run_time = 1),
        	ShowCreation(puntos2[len(puntos2)-1]),
        	FadeOut(recta1),
        	FadeOut(puntos2[len(puntos2)-2]),
        )

        recta3 = recta(ejes1, (1-math.sqrt(21))/2, 1.486831897, graph12, graph11)

        puntos2.add(posicion(ejes1, 1.486831897, curva_eliptica1[0], "$R2$"))

        self.play(
        	ShowCreation(recta3, rate_func = linear, run_time = 1),
        	ShowCreation(puntos2[len(puntos2)-1]),
        	FadeOut(recta2),
        	FadeOut(puntos2[len(puntos2)-2]),
        )

        recta4 = recta(ejes1, 1.486831897, 1.486831897, graph11, graph12)

        puntos2.add(posicion(ejes1, 1.486831897, curva_eliptica1[1], "$P+(Q+C)$", DOWN))
        
        self.play(
        	ShowCreation(recta4, rate_func = linear, run_time = 1),
        	ShowCreation(puntos2[len(puntos2)-1]),
        	FadeOut(recta3),
        	FadeOut(puntos2[len(puntos2)-2]),
        )

        Titulo2 = TextMobject("$P+(Q+C)$")
        Titulo2.to_corner(DOWN + LEFT)

        self.play(
        	ShowCreation(Titulo2,run_time=3),
        	FadeOut(recta4),
        	)

        self.wait(3)

       	#self.play(todo.arrange, ORIGIN)

        #SumadePuntos(self)
    	#self.clear()
    	#self.setup_axes(animate = True)
