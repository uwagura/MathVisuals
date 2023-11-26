from manim import *
# import numpy as np

class rp1(Scene):
    def construct(self):
        # Define objects and their positions
        grid = NumberPlane()
        self.play(Create(grid))
        top = Arc(angle=PI,color=YELLOW,stroke_width = 8)
        bottom = Arc(angle=-PI,color=YELLOW,stroke_width = 8)
        self.play(Create(top))
        self.play(Create(bottom))

        # Explain equivalence relation
        definition = Tex(
            "$\mathbb{RP}^{n} = \mathbb{R}^{n+1}-\{0\}$ under the equivalence relation $x ~ \lambda x$ for $\lambda \in \mathbb{R}$",
            font_size = 32)
        definition.to_corner(UP + LEFT)
        self.play(Write(definition))

        # Define equivalent points on circle, arrow connecting them
        for i in range(10):
            nuLine = Line(start = np.array([2*np.cos(PI/2+(i*PI)/5),2*np.sin(PI/2+(i*PI)/5),0]),
                            end = np.array([-2*np.cos(PI/2+(i*PI)/5),-2*np.sin(PI/2+(i*PI)/5),0]))
            self.play(Create(nuLine))
            self.remove(nuLine)

        self.remove(definition)
        equiv_explain = Tex(
            "Equivalently, $\mathbb{RP}^{n}$ can be formed by identifying antipodal points on $S^{n}$",
            font_size = 32)
        equiv_explain.to_corner(UP + LEFT)
        self.play(Write(equiv_explain))

        # Combine equivalent points
        self.play(Transform(bottom, top))
        
        # Mention Homotopy
        self.remove(equiv_explain)
        homot_explain = Tex(
            "In $\mathbb{R}^{2}$, $\mathbb{RP}^{1}$ is homeomorphic to $\mathbb{S}^{1}$",
            font_size = 32)
        homot_explain.to_corner(UP + LEFT)
        self.play(Write(homot_explain))
        
        # self.remove(bottom)
        l = Arc(start_angle=PI,angle=PI/2,stroke_width = 8,color = YELLOW)
        r = Arc(angle=-PI/2,stroke_width = 8,color = YELLOW)
        self.play(Create(l),Create(r))

        # # Rotate elements together
        # self.play(Rotate(equivalence,-PI/4,about_point=ORIGIN))
        # self.play(Rotate(equivalence,PI/2,about_point=ORIGIN))
        # self.play(Rotate(equivalence,-PI/4,about_point=ORIGIN))
        self.wait(2)
 
