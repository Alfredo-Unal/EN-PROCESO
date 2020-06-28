from manimlib.imports import *

class SumadePuntos(GraphScene):
    CONFIG = {
        "y_max" : 4,
        "y_min" : -4,
        "x_max" : 4,
        "x_min" : -4,
        "y_tick_frequency" : 2,
        "x_tick_frequency" : 2,
        "axes_color" : BLUE,
        "graph_origin" : ORIGIN,
    }

    def construct(self):

        self.setup_axes(animate = True)

        graph2 = self.get_graph(lambda x : math.sqrt(x**3 - 2*x + 3),
                                    color = GREEN,
                                    x_min = -1.8932891963044975,
                                    x_max = 2.7
                                    )

        graph1 = self.get_graph(lambda x : -math.sqrt(x**3 - 2*x + 3),
                                    color = GREEN,
                                    x_min = -1.8932891963044975,
                                    x_max = 2.7
                                    )

        ecuacion = TextMobject("$y^2 = x^3 - 2x + 3$")
        ecuacion.to_corner(UL)

        self.play(
            ShowCreation(graph2),
            ShowCreation(graph1),
            ShowCreation(ecuacion),
            run_time = 2,
        )
        self.wait()

        punto1 = Dot()
        vector1 = self.input_to_graph_point(1,graph2)
        punto1.move_to(vector1) #con respecto a origen
        texto1 = TexMobject("a")
        texto1.next_to(vector1, UP) #con respecto a vector1

        punto2 = Dot()
        vector2 = self.input_to_graph_point(2,graph2)
        punto2.move_to(vector2)
        texto2 = TexMobject("b")
        texto2.next_to(vector2,UP)

        self.play(
            ShowCreation(punto1),
            ShowCreation(punto2),
            ShowCreation(texto1),
            ShowCreation(texto2))

        graph3 = ParametricFunction(
            lambda u: u*vector1 + (1-u)*vector2
                , color = RED, t_min = -1.2, t_max = 3.5
            )

        graph4 = self.get_graph(lambda x : x*( math.sqrt(7) - math.sqrt(2) ) - math.sqrt(7) + 2*math.sqrt(2),
                                    color = GREEN,
                                    x_min = -2,
                                    x_max = 4
                                    )

        self.play(ShowCreation(graph3))

        punto3 = Dot()
        vector3 = self.input_to_graph_point(6-2*math.sqrt(14),graph4)
        punto3.move_to(vector3)
        texto3 = TexMobject("c")
        texto3.next_to(vector3,UP)

        self.play(
            ShowCreation(punto3),
            ShowCreation(texto3))
        self.wait()

        punto4 = Dot()
        vector4 = self.input_to_graph_point(6-2*math.sqrt(14),graph2)
        punto4.move_to(vector4)
        texto4 = TexMobject("a + b")
        texto4.next_to(vector4,UP)

        graph5 = ParametricFunction(
            lambda u: (1-u)*vector4 + u*vector3
                , color = RED, t_min = 0, t_max = 1
            )

        self.play(
            ReplacementTransform(graph3,graph5))
        self.wait()

        self.play(
            ShowCreation(punto4),
            ShowCreation(texto4))
        self.wait()

        #Desde acá empiezo a programar io, Roger, la máquina, la fiera, el mastodonte, el maestro, el artista
        #Graph2 = positive
        #Graph1 = negative

        posSig = self.input_to_graph_point(-math.sqrt(2/3), graph2)
        posC = self.coords_to_point(2*math.sqrt(2/3), (1/3)*math.sqrt(27 +4*math.sqrt(6)))
        posS = self.coords_to_point(2*math.sqrt(2/3), -(1/3)*math.sqrt(27 + 4*math.sqrt(6)))

        point1 = Dot().move_to ( posSig )
        point1C = Dot().move_to ( posC )
        point1S = Dot().move_to ( posS )

        textA = TexMobject("a")
        textB = TexMobject("b")
        textC = TexMobject("c")
        textAB = TexMobject("a + b")
        textA.next_to (posSig, UP)
        textB.next_to (posSig, DOWN)
        textC.next_to (posC, UP)
        textAB.next_to (posS, DOWN)

        graphTAN = ParametricFunction ( lambda u: u*posC + (1-u)*posSig,
                                        color = RED, t_min = -1.3, t_max = 1)
        graphRFL = ParametricFunction ( lambda u: (1-u)*posS + u*posC,
                                        color = RED, t_min = 0, t_max = 1)
        
        self.play( ReplacementTransform (punto1,point1),
                   ReplacementTransform (punto2,point1),
                   ReplacementTransform (texto1, textA),
                   ReplacementTransform (texto2, textB),
                   FadeOut(texto3),
                   FadeOut(texto4),
                   FadeOut(punto3),
                   FadeOut(punto4),
                   FadeOut(graph5))
        self.wait ()

        self.play (ShowCreation (graphTAN))

        self.play (ShowCreation (point1C), ShowCreation(textC))

        self.wait()

        self.play(ReplacementTransform (graphTAN, graphRFL))
        
        self.play (ShowCreation (point1S), ShowCreation(textAB))
        self.wait()

        finPosA = posSig
        finPosB = self.input_to_graph_point(-math.sqrt(2/3), graph1)


        finTextA = TexMobject("a")
        finTextA.next_to (finPosA, LEFT)
        finTextB = TexMobject("b")
        finTextB.next_to (finPosB, LEFT)
        pointB = Dot().move_to ( finPosB )

        graphVer = ParametricFunction ( lambda u: u*finPosB + (1-u)*finPosA,
                                        color = RED, t_min = -0.5, t_max = 1.5)
        

        self.play (ShowCreation (pointB),
                   ReplacementTransform (textA, finTextA),
                   ReplacementTransform (textB, finTextB),
                   FadeOut(point1C),
                   FadeOut(textC),
                   FadeOut(point1S),
                   FadeOut(textAB),
                   FadeOut(graphRFL))

        self.play (ShowCreation(graphVer) )
        self.wait()

        textFinal = TexMobject("\mathcal{O}")
        textFinal.next_to ( finPosA, 3*UP + RIGHT)

        self.play (ShowCreation(textFinal))
        self.wait ()
        

        
        

class Asociatividad(GraphScene):
    def construct(self):
        ejes1 = Axes(
            x_min = -4, x_max = 4,
            y_min = -4, y_max = 4,
            center_point = LEFT*3,
            x_axis_config = {
                "tick_frequency" : 1,
                "color" : DARK_BLUE,
                "unit_size": .7,
            },
            y_axis_config = {
                "tick_frequency" : 1,
                "color" : DARK_BLUE,
                "unit_size": .7,
            },

        )
        #ejes1.add_coordinates()

        ejes2 = Axes(
            x_min = -4, x_max = 4,
            y_min = -4, y_max = 4,
            center_point = RIGHT*3,
            x_axis_config = {
                "tick_frequency" : 1,
                "color" : DARK_BLUE,
                "unit_size": .7,
            },
            y_axis_config = {
                "tick_frequency" : 1,
                "color" : DARK_BLUE,
                "unit_size": .7,
            },

        )
        #ejes2.add_coordinates()

        graph11 = ejes1.get_graph(lambda x : math.sqrt(x**3 - 2*x + 3),
                                    color = GREEN,
                                    x_min = -1.8932891963044975,
                                    x_max = 2.7
                                    )

        graph12 = ejes1.get_graph(lambda x : -math.sqrt(x**3 - 2*x + 3),
                                    color = GREEN,
                                    x_min = -1.8932891963044975,
                                    x_max = 2.7
                                    )

        graph21 = ejes2.get_graph(lambda x : math.sqrt(x**3 - 2*x + 3),
                                    color = GREEN,
                                    x_min = -1.8932891963044975,
                                    x_max = 2.7
                                    )

        graph22 = ejes2.get_graph(lambda x : -math.sqrt(x**3 - 2*x + 3),
                                    color = GREEN,
                                    x_min = -1.8932891963044975,
                                    x_max = 2.7
                                    )

        grafica1 = VGroup(ejes1, graph11, graph12) #lista de Mobject
        grafica2 = VGroup(ejes2, graph21, graph22)

        self.play(
            ShowCreation(grafica1,run_time = 5),
            ShowCreation(grafica2,run_time = 5),
        )
        self.wait(1)

        punto11 = Dot(
            ejes1.input_to_graph_point(1,graph11)[0]*RIGHT + ejes1.input_to_graph_point(1,graph11)*UP)
        texto11 = TexMobject("P")
        texto11.scale (0.5)
        texto11.next_to(ejes1.input_to_graph_point(1,graph11),UP)

        Punto11 = VGroup(punto11,texto11)

        punto12 = Dot(
            ejes1.input_to_graph_point(2,graph11)[0]*RIGHT + ejes1.input_to_graph_point(2,graph11)*UP)
        texto12 = TexMobject("Q")
        texto12.scale (0.5)
        texto12.next_to(ejes1.input_to_graph_point(2,graph11),UP)

        Punto12 = VGroup(punto12,texto12)

        punto13 = Dot(
            ejes1.input_to_graph_point(6-2*math.sqrt(14),graph12)[0]*RIGHT + ejes1.input_to_graph_point(6-2*math.sqrt(14),graph12)*UP)
        texto13 = TexMobject("R_2")
        texto13.scale (0.5)
        texto13.next_to(ejes1.input_to_graph_point(6-2*math.sqrt(14),graph12),UP)

        Punto13 = VGroup(punto13,texto13)

        punto14 = Dot(
            ejes1.input_to_graph_point(0,graph11)[0]*RIGHT + ejes1.input_to_graph_point(0,graph11)[1]*UP)
        texto14 = TexMobject("C")
        texto14.scale (0.5)
        texto14.next_to(ejes1.input_to_graph_point(0,graph11),UP)

        Punto14 = VGroup(punto14,texto14)

        puntos1 = VGroup(Punto11, Punto12, Punto14)

        punto21 = Dot(
            ejes2.input_to_graph_point(1,graph21)[0]*RIGHT + ejes2.input_to_graph_point(1,graph21)*UP)
        texto21 = TexMobject("P")
        texto21.scale (0.5)
        texto21.next_to(ejes2.input_to_graph_point(1,graph21),UP)

        Punto21 = VGroup(punto21,texto21)

        punto22 = Dot(
            ejes2.input_to_graph_point(2,graph21)[0]*RIGHT + ejes2.input_to_graph_point(2,graph21)*UP)
        texto22 = TexMobject("Q")
        texto22.scale (0.5)
        texto22.next_to(ejes2.input_to_graph_point(2,graph21),UP)

        Punto22 = VGroup(punto22,texto22)

        punto23 = Dot(
            ejes2.input_to_graph_point(6-2*math.sqrt(14),graph22)[0]*RIGHT + ejes2.input_to_graph_point(6-2*math.sqrt(14),graph22)*UP)
        texto23 = TexMobject("S_1")
        texto23.scale (0.5)
        texto23.next_to(ejes2.input_to_graph_point(6-2*math.sqrt(14),graph22),UP)

        Punto23 = VGroup(punto23,texto23)

        punto24 = Dot(
            ejes2.input_to_graph_point(0,graph21)[0]*RIGHT + ejes2.input_to_graph_point(0,graph21)[1]*UP)
        texto24 = TexMobject("C")
        texto24.scale (0.5)
        texto24.next_to(ejes2.input_to_graph_point(0,graph21),UP)

        Punto24 = VGroup(punto24,texto24)

        punto25 = Dot(
            ejes2.input_to_graph_point(6-2*math.sqrt(14),graph21)[0]*RIGHT + ejes2.input_to_graph_point(6-2*math.sqrt(14),graph21)*UP)
        texto25 = TexMobject("P+Q")
        texto25.scale (0.5)
        texto25.next_to(ejes2.input_to_graph_point(6-2*math.sqrt(14),graph21),UP)

        Punto25 = VGroup(punto25,texto25)

        punto26 = Dot(
            ejes2.input_to_graph_point(1.486831897,graph21)[0]*RIGHT + ejes2.input_to_graph_point(1.486831897,graph21)*UP)
        texto26 = TexMobject("S_2")
        texto26.scale (0.5)
        texto26.next_to(ejes2.input_to_graph_point(1.486831897,graph21),UP)

        Punto26 = VGroup(punto26,texto26)

        punto27 = Dot(
            ejes2.input_to_graph_point(1.486831897,graph22)[0]*RIGHT + ejes2.input_to_graph_point(1.486831897,graph22)*UP)
        texto27 = TexMobject("(P+Q)+C")
        texto27.scale (0.5)
        texto27.next_to(ejes2.input_to_graph_point(1.486831897,graph22),UP)

        Punto27 = VGroup(punto27,texto27)

        puntos2 = VGroup(Punto21, Punto22, Punto24)

        self.play(ShowCreation(puntos1,run_time = 2),
            ShowCreation(puntos2, run_time = 2))
        self.wait(1)

        graph23 = ParametricFunction(
            lambda u: u*(ejes2.input_to_graph_point(1,graph21)) + (1-u)*ejes2.input_to_graph_point(2,graph21)
                , color = RED, t_min = 0, t_max = 3.5
            )

        self.play(
            ShowCreation(graph23,run_time = 2),
            ShowCreation(Punto23,run_time = 1.5),
            )

        graph24 = ParametricFunction(
            lambda u: u*(ejes2.input_to_graph_point(6-2*math.sqrt(14),graph22)) + (1-u)*ejes2.input_to_graph_point(6-2*math.sqrt(14),graph21)
                , color = RED, t_min = 0, t_max = 1
            )

        self.play(
            ReplacementTransform(graph23,graph24),
            ShowCreation(Punto25,run_time = 1.5),
            )

        graph25 = ParametricFunction(
            lambda u: (1-u)*(ejes2.input_to_graph_point(6-2*math.sqrt(14),graph21)) + (u)*ejes2.input_to_graph_point(1.486831897,graph21)
                , color = RED, t_min = 0, t_max = 1
            )

        self.play(
            ReplacementTransform(graph24,graph25),
            ShowCreation(Punto26,run_time = 1.5),
            )

        graph26 = ParametricFunction(
            lambda u: (u)*ejes2.input_to_graph_point(1.486831897,graph21) + (1-u)*ejes2.input_to_graph_point(1.486831897,graph22)
                , color = RED, t_min = 0, t_max = 1
            )

        self.play(
            ReplacementTransform(graph25,graph26),
            ShowCreation(Punto27,run_time = 1.5),
            )


        self.wait(5)
