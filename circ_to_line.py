from manim import *

class CircToLine(Scene):
    def construct(self):
        # Define objects and their positions
        circle = Circle(color=YELLOW)
        real_line = NumberLine(
            x_range=[-10, 10, 2],
            length=9,
            color=BLUE,
            include_numbers=True,
            label_direction=UP
        )
        real_line.next_to(circle,UP,buff=-0.1)
        real_line.shift([-0.125,0,0])

        # Define points on circle, arrow connecting them, and combine in group
        p1 = Dot(point=circle.point_at_angle(PI/2))
        p2 = Dot(point=circle.point_at_angle(-PI/2))
        p1.set_color(RED)
        p2.set_color(RED)
        # map = Arrow(start = DOWN, end = UP, buff =0, max_stroke_width_to_length_ratio = 2)
        map = Line(start = DOWN, end = UP, buff =0)
        pguide1 = real_line.n2p(-1)
        pguide2 = real_line.n2p(1)
        circ_to_line = VGroup(p1,p2)


        # Have objects appear one by one
        self.play(Create(circle))
        self.play(Create(real_line))
        self.play(Create(p1))
        self.play(Create(p2))
        self.play(Create(map))

        # Rotate points and vectors
        map.add_updater(lambda m: m.set_points_by_ends(p2.get_center(), 
                            line_intersection(
                                [p1.get_center(),p2.get_center()],
                                [pguide1,pguide2]
                            )))
        self.play(Rotate(circ_to_line,-PI/4-PI/8-PI/16,about_point=ORIGIN))
        self.play(Rotate(circ_to_line,PI/2+PI/4+PI/8,about_point=ORIGIN))
        self.play(Rotate(circ_to_line,-PI/4-PI/8-PI/16,about_point=ORIGIN))
        self.wait(5)
 
