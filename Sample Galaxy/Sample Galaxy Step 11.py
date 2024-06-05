import tkinter as tk
import random
import math

class SampleGalaxyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sample Galaxy")
        
        self.canvas = tk.Canvas(root, width=1800, height=1200, bg="black")
        self.canvas.pack()

        self.angle_offset = 60  # Initial angle offset for the spiral arms
        self.time = 1000  # Time counter for slow modulation

        self.create_galaxy_view()
        self.animate_galaxy()

    def create_galaxy_view(self):
        # Clear canvas and destroy existing buttons
        self.canvas.delete("all")

        # Draw spiral galaxy
        self.draw_spiral_galaxy(angle_offset=self.angle_offset)

    def draw_spiral_galaxy(self, angle_offset):
        num_arms = 8  # Number of arms in the spiral galaxy
        num_stars_per_arm = 200  # Number of stars per arm
        arm_length = 200  # Length of each arm
        center_x, center_y = 900, 600  # Center of the galaxy
        flatten_factor = -.5  # Flatten factor for the side view
        arm_thickness = 15  # Thickness of the arms

        for arm in range(num_arms):
            for i in range(num_stars_per_arm):
                angle = (i / num_stars_per_arm) * 2 * math.pi  # Angle around the center

                # Calculate the distance from the center for each star
                distance_from_center = arm_length * (1 + i / num_stars_per_arm) +600

                # Slow modulation over time
                distance_modulation = math.sin(self.time + i * 0.1) * 80  # Slower modulation
                distance_from_center += distance_modulation

                # Calculate the position of the star with adjusted angle offset
                x = center_x + distance_from_center * math.cos(angle - arm * 2 * math.pi / num_arms - angle_offset / 2)
                y = center_y + distance_from_center * math.sin(angle - arm * 2 * math.pi / num_arms - angle_offset / 2) * flatten_factor

                # Draw the star
                size = random.randint(1, 1)
                self.canvas.create_oval(x - size, y - size, x + size, y + size, fill="white", outline="")

    def animate_galaxy(self):
        # Animate the rotation of the galaxy
        self.angle_offset += 0.01  # Increment the angle offset for rotation
        self.time += 0.05  # Increment time for modulation
        self.create_galaxy_view()  # Redraw the galaxy with the updated angle offset
        self.root.after(50, self.animate_galaxy)  # Repeat the animation every 50 milliseconds

    def magnetize_star_system(self, system):
        # Placeholder for magnetizing a star system to a point on one of the arms
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = SampleGalaxyApp(root)
    root.mainloop()
