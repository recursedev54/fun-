import tkinter as tk
import random
import numpy as np

def hex_to_rgb_and_alpha(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 8:
        raise ValueError("Input should be an 8-digit hex code.")
    
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    a = int(hex_color[6:8], 16)
    return (r, g, b, a)

def create_oval_with_alpha(canvas, x1, y1, x2, y2, fill):
    r, g, b, a = hex_to_rgb_and_alpha(fill)
    color = f'#{r:02x}{g:02x}{b:02x}'
    alpha = a / 255.0
    
    # Create the oval with background color
    oval = canvas.create_oval(x1, y1, x2, y2, fill=color, outline="")
    
    # Apply transparency using built-in stipple patterns
    if alpha > 0.75:
        stipple_pattern = "gray25"
    elif alpha > 0.5:
        stipple_pattern = "gray50"
    elif alpha > 0.25:
        stipple_pattern = "gray75"
    else:
        stipple_pattern = ""
    
    canvas.itemconfig(oval, stipple=stipple_pattern)
    
    return oval

class SampleGalaxyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sample Galaxy")
        
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()
        
        self.angle_offset = 60  # Initial angle offset for the spiral arms
        self.time = 0  # Time counter for slow modulation
        self.rotation_counter = 0  # Counter for rotation updates
        self.color_update_interval = 10  # Update colors every 10 rotations

        self.stars = []  # List to store star objects
        self.create_galaxy_view()
        self.animate_rotation()

    def create_galaxy_view(self):
        # Clear canvas
        self.canvas.delete("all")
        self.stars = []

        # Draw spiral galaxy
        self.draw_spiral_galaxy(angle_offset=self.angle_offset)

    def draw_spiral_galaxy(self, angle_offset):
        num_arms = 5  # Number of arms in the spiral galaxy
        num_stars_per_arm = 100  # Number of stars per arm
        arm_length = 300  # Length of each arm
        center_x, center_y = 400, 300  # Center of the galaxy
        flatten_factor = 0.5  # Flatten factor for the side view
        arm_thickness = 2  # Thickness of the arms

        angles = np.linspace(0, 2 * np.pi, num_stars_per_arm)
        for arm in range(num_arms):
            distance_modulation = np.sin(self.time + np.arange(num_stars_per_arm) * 0.1) * 50  # Slower modulation
            distance_from_center = arm_length * (1 + np.arange(num_stars_per_arm) / num_stars_per_arm) - 188 + distance_modulation

            x_bases = center_x + distance_from_center * np.cos(angles - arm * 2 * np.pi / num_arms - angle_offset / 2)
            y_bases = center_y + distance_from_center * np.sin(angles - arm * 2 * np.pi / num_arms - angle_offset / 2) * flatten_factor

            for i in range(num_stars_per_arm):
                x_base = x_bases[i]
                y_base = y_bases[i]

                x = x_base + random.uniform(-arm_thickness, arm_thickness)
                y = y_base + random.uniform(-arm_thickness, arm_thickness) * flatten_factor

                # Draw the star with random color and transparency
                color = "#{:02x}{:02x}{:02x}{:02x}".format(
                        #protantan set
                    random.randint(0, 100), # red
                    random.randint(50, 255), # green
                    random.randint(50, 100), # blue
                    random.randint(100, 255)  # Random transparency
                    #tritan set
                #    random.randint(50, 255), # red
                #    random.randint(50, 255), # green
                #    random.randint(0, 100), # blue
                #    random.randint(100, 255)  # Random transparency
                    #deutan set
                #    random.randint(0, 200), # red
                #    random.randint(0, 200), # green
                #    random.randint(100, 255), # blue
                #    random.randint(100, 255)  # Random transparency
                )
                size = random.uniform(1, 3)  # Random size for stars
                oval = create_oval_with_alpha(self.canvas, x - size, y - size, x + size, y + size, fill=color)
                self.stars.append(oval)

    def animate_rotation(self):
        # Animate the rotation of the galaxy
        self.angle_offset += 0.10  # Increment the angle offset for rotation
        self.time += 0.05  # Increment time for modulation

        # Increment rotation counter
        self.rotation_counter += 1

        # Update colors and redraw galaxy every 'color_update_interval' rotations
        if self.rotation_counter >= self.color_update_interval:
            self.create_galaxy_view()  # Redraw the galaxy with updated colors
            self.rotation_counter = 0  # Reset rotation counter
        else:
            # Only update positions of stars without changing colors
            num_arms = 5  # Number of arms in the spiral galaxy
            num_stars_per_arm = 100  # Number of stars per arm
            arm_length = 300  # Length of each arm
            center_x, center_y = 400, 300  # Center of the galaxy
            flatten_factor = 0.5  # Flatten factor for the side view
            arm_thickness = 2  # Thickness of the arms

            angles = np.linspace(0, 2 * np.pi, num_stars_per_arm)
            star_index = 0
            for arm in range(num_arms):
                distance_modulation = np.sin(self.time + np.arange(num_stars_per_arm) * 0.1) * 50  # Slower modulation
                distance_from_center = arm_length * (1 + np.arange(num_stars_per_arm) / num_stars_per_arm) - 188 + distance_modulation

                x_bases = center_x + distance_from_center * np.cos(angles - arm * 2 * np.pi / num_arms - self.angle_offset / 2)
                y_bases = center_y + distance_from_center * np.sin(angles - arm * 2 * np.pi / num_arms - self.angle_offset / 2) * flatten_factor

                for i in range(num_stars_per_arm):
                    x_base = x_bases[i]
                    y_base = y_bases[i]

                    x = x_base + random.uniform(-arm_thickness, arm_thickness)
                    y = y_base + random.uniform(-arm_thickness, arm_thickness) * flatten_factor

                    # Update the position of the existing star
                    size = 3  # Size used in the create_oval_with_alpha function
                    self.canvas.coords(self.stars[star_index], x - size, y - size, x + size, y + size)
                    star_index += 1

        self.root.after(50, self.animate_rotation)  # Repeat the rotation animation every 50 milliseconds

if __name__ == "__main__":
    root = tk.Tk()
    app = SampleGalaxyApp(root)
    root.mainloop()



    
