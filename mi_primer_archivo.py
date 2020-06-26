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
        "y_labeled_nums": range(-4,4,1),
        "x_labeled_nums": range(-4,4,1),
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
                , color = RED, t_min = 0, t_max = 3.5
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
            lambda u: u*vector4 + (1-u)*vector3
                , color = RED, t_min = 0, t_max = 1
            )

        self.play(
            ReplacementTransform(graph3,graph5))
        self.wait()

        self.play(
            ShowCreation(punto4),
            ShowCreation(texto4))
        self.wait()

class Asociatividad(GraphScene):
    def construct(self):
        ejes1 = Axes(
            x_min = -4, x_max = 4,
            y_min = -4, y_max = 4,
            center_point = LEFT*3,
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
        ejes1.add_coordinates()

        ejes2 = Axes(
            x_min = -4, x_max = 4,
            y_min = -4, y_max = 4,
            center_point = RIGHT*3,
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
        ejes2.add_coordinates()

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
        self.wait(2)

        punto11 = Dot(
            ejes1.input_to_graph_point(1,graph11)[0]*RIGHT + ejes1.input_to_graph_point(1,graph11)*UP)

        punto12 = Dot(
            ejes1.input_to_graph_point(2,graph11)[0]*RIGHT + ejes1.input_to_graph_point(2,graph11)*UP)

        punto13 = Dot(
            ejes1.input_to_graph_point(6-2*math.sqrt(14),graph12)[0]*RIGHT + ejes1.input_to_graph_point(6-2*math.sqrt(14),graph12)*UP)

        punto14 = Dot(
            ejes1.input_to_graph_point(0,graph11)[0]*RIGHT + ejes1.input_to_graph_point(0,graph11)[1]*UP)

        puntos1 = VGroup(punto11, punto12, punto14)

        punto21 = Dot(
            ejes2.input_to_graph_point(1,graph21)[0]*RIGHT + ejes2.input_to_graph_point(1,graph21)*UP)

        punto22 = Dot(
            ejes2.input_to_graph_point(2,graph21)[0]*RIGHT + ejes2.input_to_graph_point(2,graph21)*UP)

        punto23 = Dot(
            ejes2.input_to_graph_point(6-2*math.sqrt(14),graph22)[0]*RIGHT + ejes2.input_to_graph_point(6-2*math.sqrt(14),graph22)*UP)

        punto24 = Dot(
            ejes2.input_to_graph_point(0,graph21)[0]*RIGHT + ejes2.input_to_graph_point(0,graph21)[1]*UP)

        puntos2 = VGroup(punto21, punto22, punto24)

        self.play(ShowCreation(puntos1,run_time = 3), ShowCreation(puntos2, run_time = 3))
        self.wait(5)
