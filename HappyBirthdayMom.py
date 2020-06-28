from manimlib.imports import *

def heartPoint (self, t):
        return self.coords_to_point (16/7*pow(math.sin(t),3),
                                          1/5*(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t) ))

class HearthMessage(GraphScene):
    CONFIG = {
        "y_max" : 5,
        "y_min" : -5,
        "x_max" : 5,
        "x_min" : -5,
        "y_tick_frequency" : 2,
        "x_tick_frequency" : 1,
        "x_axis_label": None,
        "y_axis_label": None,
        "axes_color" : BLUE,
        "graph_origin" : ORIGIN,
    }

    

    def construct (self):

        self.setup_axes (animate = True)
        
        heartR = ParametricFunction ( lambda t: heartPoint(self,t), color = RED, t_min = 0, t_max = PI)
        heartL = ParametricFunction ( lambda t: heartPoint(self,-t), color = RED, t_min = 0, t_max = PI)

        mensaje1 = TextMobject ( "Feliz Cumplea\~nos " )
        mensaje2 = TextMobject ( "Mam\\'a")
        mensaje2.set_color_by_tex("Mam\\'a", RED)
        mensaje = VGroup (mensaje1,mensaje2)
        mensaje.arrange_submobjects(DOWN, buff=SMALL_BUFF)
        mensaje.to_corner (UR)
        
        self.play ( Write (mensaje), run_time = 2)
        self.play ( ShowCreation ( heartR ), ShowCreation ( heartL ) , run_time=3)


