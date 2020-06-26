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

        graph11 = ParametricFunction(
            lambda u: np.array([
            u,
            math.sqrt(u**3 - 2*u + 3),
            0]),
            color = RED, t_min = -1.8932891963044975, t_max = 2
            ).shift(LEFT*3)

        graph12 = ParametricFunction(
            lambda u: np.array([
            u,
            -math.sqrt(u**3 - 2*u + 3),
            0]),
            color = RED, t_min = -1.8932891963044975, t_max = 2
            ).shift(LEFT*3)

        graph21 = ParametricFunction(
            lambda u: np.array([
            u,
            math.sqrt(u**3 - 2*u + 3),
            0]),
            color = RED, t_min = -1.8932891963044975, t_max = 2
            ).shift(RIGHT*3)

        graph22 = ParametricFunction(
            lambda u: np.array([
            u,
            -math.sqrt(u**3 - 2*u + 3),
            0]),
            color = RED, t_min = -1.8932891963044975, t_max = 2
            ).shift(RIGHT*3)

        #graph31 = self.get_graph(
        #    lambda x : math.sqrt(x**3 - 2*x + 3),
        #            color = GREEN,
        #            x_min = -1.8932891963044975,
        #            x_max = 2.7
        #    ).shift(RIGHT*3)

        grafica1 = VGroup(graph11, graph12, ejes1) #lista de Mobject
        grafica2 = VGroup(ejes2, graph21, graph22)

        self.play(
            ReplacementTransform(grafica1, grafica2),
        )

        self.wait(2)
        #self.clear()
        #self.play(
        #    ShowCreation(graph11),
        #    ShowCreation(graph12),
        #    ShowCreation(ejes1),
        #    ShowCreation(ejes2),
        #    ShowCreation(graph21),
        #    ShowCreation(graph22),
        #    )
        #self.wait(2)

        punto11 = Dot()
        #vector11 = self.input_to_graph_point(1,graph12)
        #punto11.move_to(vector11)


        self.add(punto11)
        self.wait()
