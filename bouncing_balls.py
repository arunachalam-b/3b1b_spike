from manim import *
import numpy as np

class BouncingBalls(Scene):
    def construct(self):
        # Properties
        num_balls = 5
        ball_radius = 0.2
        ball_colors = [BLUE, GREEN, YELLOW, RED, PURPLE]
        elasticity = 0.8

        screen_width = config.frame_width
        screen_height = config.frame_height
        wall_buffer = 0.5
        min_x = -screen_width / 2 + wall_buffer
        max_x = screen_width / 2 - wall_buffer
        min_y = -screen_height / 2 + wall_buffer
        max_y = screen_height / 2 - wall_buffer
        gravity = np.array([0, -9.8, 0])

        # Remove placeholder
        # title = Text("Bouncing Balls Animation", font_size=48)
        # self.play(Write(title))
        # self.wait(1)

        balls = []
        for i in range(num_balls):
            chosen_color = ball_colors[i % len(ball_colors)]
            start_x = np.random.uniform(min_x + ball_radius, max_x - ball_radius)
            start_y = np.random.uniform(min_y + ball_radius, max_y - ball_radius)
            
            ball = Circle(radius=ball_radius, color=chosen_color, fill_opacity=0.8)
            ball.move_to(np.array([start_x, start_y, 0]))

            start_vx = np.random.uniform(-2, 2)
            start_vy = np.random.uniform(-2, 2)
            ball.velocity = np.array([start_vx, start_vy, 0])
            
            balls.append(ball)
            self.add(ball)

        def update_ball(ball, dt):
            # Update velocity due to gravity
            ball.velocity += gravity * dt
            # Update position
            ball.move(ball.velocity * dt)

            ball_center = ball.get_center()
            
            # Collision with vertical walls (X-axis)
            if ball_center[0] - ball_radius < min_x:
                ball.move_to(np.array([min_x + ball_radius, ball_center[1], 0]))
                ball.velocity[0] = -ball.velocity[0] * elasticity
            elif ball_center[0] + ball_radius > max_x:
                ball.move_to(np.array([max_x - ball_radius, ball_center[1], 0]))
                ball.velocity[0] = -ball.velocity[0] * elasticity

            # Collision with horizontal walls (Y-axis)
            if ball_center[1] - ball_radius < min_y:
                ball.move_to(np.array([ball_center[0], min_y + ball_radius, 0]))
                ball.velocity[1] = -ball.velocity[1] * elasticity
            elif ball_center[1] + ball_radius > max_y:
                ball.move_to(np.array([ball_center[0], max_y - ball_radius, 0]))
                ball.velocity[1] = -ball.velocity[1] * elasticity

        for ball in balls:
            ball.add_updater(update_ball)

        self.wait(20)
