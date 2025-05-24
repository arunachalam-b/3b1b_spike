from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Title
        title = Text("Pythagorean Theorem", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create a right triangle with sides 3, 4, 5
        triangle = Polygon(
            [-3, -1.5, 0],  # Bottom left
            [1, -1.5, 0],   # Bottom right  
            [-3, 1.5, 0],   # Top left
            color=WHITE,
            fill_opacity=0.3,
            fill_color=GRAY
        )
        
        # Add the triangle
        self.play(Create(triangle))
        self.wait(0.5)
        
        # Label the sides
        side_a = Text("a = 3", font_size=24, color=RED).next_to(triangle.get_left(), LEFT)
        side_b = Text("b = 4", font_size=24, color=GREEN).next_to(triangle.get_bottom(), DOWN)
        side_c = Text("c = 5", font_size=24, color=BLUE).next_to(triangle.get_edge_center(UR), UR)
        
        self.play(Write(side_a), Write(side_b), Write(side_c))
        self.wait(1)
        
        # Create squares on each side
        # Square on side a (3x3)
        square_a = Square(side_length=3, color=RED, fill_opacity=0.5, fill_color=RED)
        square_a.next_to(triangle.get_left(), LEFT, buff=0)
        
        # Square on side b (4x4)
        square_b = Square(side_length=4, color=GREEN, fill_opacity=0.5, fill_color=GREEN)
        square_b.next_to(triangle.get_bottom(), DOWN, buff=0)
        
        # Square on side c (5x5) - positioned on hypotenuse
        square_c = Square(side_length=5, color=BLUE, fill_opacity=0.5, fill_color=BLUE)
        square_c.move_to([2, 1, 0])
        
        # Animate the squares appearing
        self.play(FadeIn(square_a))
        self.wait(0.3)
        self.play(FadeIn(square_b))
        self.wait(0.3)
        self.play(FadeIn(square_c))
        self.wait(1)
        
        # Show the areas
        area_a = Text("Area = 9", font_size=20, color=WHITE).move_to(square_a.get_center())
        area_b = Text("Area = 16", font_size=20, color=WHITE).move_to(square_b.get_center())
        area_c = Text("Area = 25", font_size=20, color=WHITE).move_to(square_c.get_center())
        
        self.play(Write(area_a), Write(area_b), Write(area_c))
        self.wait(1)
        
        # Show the equation
        equation = MathTex("a^2 + b^2 = c^2", font_size=36, color=YELLOW)
        equation.to_edge(DOWN)
        self.play(Write(equation))
        self.wait(0.5)
        
        # Show the numerical verification
        verification = MathTex("3^2 + 4^2 = 5^2", font_size=32, color=YELLOW)
        verification.next_to(equation, DOWN)
        self.play(Write(verification))
        self.wait(0.5)
        
        final_calc = MathTex("9 + 16 = 25", font_size=32, color=GREEN)
        final_calc.next_to(verification, DOWN)
        self.play(Write(final_calc))
        self.wait(1)
        
        # Final highlight
        self.play(
            Indicate(equation, color=YELLOW),
            Indicate(final_calc, color=GREEN)
        )
        self.wait(2) 