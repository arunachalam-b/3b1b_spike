from manim import *

class DhoniQuoteAnimation(Scene):
    def construct(self):
        # Load and display the image of MS Dhoni
        dhoni_image = ImageMobject("assets/dhoni.png")
        dhoni_image.scale(0.6)  # Scale down the image
        dhoni_image.to_edge(LEFT, buff=1)  # Position on the left side
        
        # Create a title
        title = Text("MS Dhoni", font_size=48, color=GOLD, weight=BOLD)
        title.to_edge(UP, buff=1)
        
        # Fade in the title and image
        self.play(FadeIn(title))
        self.wait(0.5)
        self.play(FadeIn(dhoni_image))
        self.wait(1)
        
        # The quote text
        quote_text = "Enjoy the game and chase your dreams. Dreams do come true."
        author_text = "- MS Dhoni"
        
        # Split the quote into words
        quote_words = quote_text.split()
        
        # Create text objects for each word
        word_objects = []
        for word in quote_words:
            word_obj = Text(word, font_size=36, color=WHITE)
            word_objects.append(word_obj)
        
        # Position the words in lines
        # First line: "Enjoy the game and chase your dreams."
        first_line_words = word_objects[:7]  # "Enjoy the game and chase your dreams."
        # Second line: "Dreams do come true."
        second_line_words = word_objects[7:]  # "Dreams do come true."
        
        # Arrange first line
        first_line = VGroup(*first_line_words)
        first_line.arrange(RIGHT, buff=0.25)
        first_line.move_to([1.8, 0.8, 0])  # Position to the right of the image
        
        # Arrange second line
        second_line = VGroup(*second_line_words)
        second_line.arrange(RIGHT, buff=0.25)
        second_line.move_to([1.8, 0.2, 0])  # Below the first line
        
        # Author attribution
        author = Text(author_text, font_size=28, color=YELLOW, slant=ITALIC)
        author.move_to([1.8, -0.6, 0])  # Below the quote
        
        # Animate words appearing one by one with fade in
        # First line
        for word in first_line_words:
            self.play(FadeIn(word), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.8)
        
        # Second line
        for word in second_line_words:
            self.play(FadeIn(word), run_time=0.6)
            self.wait(0.3)
        
        self.wait(1.5)
        
        # Show the author
        self.play(FadeIn(author), run_time=1.5)
        self.wait(2)
        
        # Add some decorative elements
        # Create a beautiful border around the quote
        quote_group = VGroup(first_line, second_line, author)
        border = SurroundingRectangle(quote_group, color=BLUE, buff=0.5, corner_radius=0.2)
        border.set_stroke(width=2, opacity=0.6)
        
        self.play(Create(border), run_time=1.5)
        self.wait(1)
        
        # Add some sparkle effects around the image
        sparkles = []
        for i in range(6):
            sparkle = Star(n=5, color=GOLD, fill_opacity=0.8).scale(0.15)
            # Position sparkles around the image
            angle = i * PI / 3
            radius = 2.5
            sparkle.move_to([radius * np.cos(angle) - 2.5, radius * np.sin(angle), 0])
            sparkles.append(sparkle)
        
        sparkle_group = VGroup(*sparkles)
        self.play(LaggedStart(*[FadeIn(sparkle) for sparkle in sparkles], lag_ratio=0.15))
        self.wait(2)
        
        # Final fade out of everything
        all_elements = Group(title, dhoni_image, first_line, second_line, author, border, sparkle_group)
        self.play(FadeOut(all_elements), run_time=3)
        self.wait(1) 