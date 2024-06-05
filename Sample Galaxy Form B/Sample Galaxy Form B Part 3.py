import tkinter as tk
import random
import math
import time

def hex_to_rgb_and_alpha(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        hex_color += 'FF'  # Add alpha channel if not provided
    elif len(hex_color) != 8:
        raise ValueError("Input should be a 6-digit or 8-digit hex code.")
    
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

class StarSystemViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Star System Viewer")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.time = 0  # Time counter for hue shifting effect
        self.hue_shift_speed = 6  # Speed of hue shifting
        self.hue_shift_factor = 4  # Hue shift factor

        self.speckle_generation_interval = 20  # Interval in milliseconds to generate new speckles
        self.speckle_shift_distance = 2  # Normal distance to shift speckles in each iteration

        self.initial_burst_speed = 10 # Speed during the initial burst phase
        self.initial_burst_generation_interval = 2  # Generation interval during the initial burst phase
        self.initial_burst_duration = 3  # Duration of the initial burst phase in seconds

        self.start_time = time.time()
        self.burst_end_time = self.start_time + self.initial_burst_duration

        self.draw_star()
        self.animate_hue_shift()
        self.animate_sideways_motion()  # Call the sideways motion animation
        self.generate_new_speckle()  # Start generating speckles continuously

    def draw_star(self):
        center_x, center_y = 400, 300
        self.star_size = 80
        self.star_center_x = center_x
        self.star_center_y = center_y

        # Draw the star base
        self.star_base = create_oval_with_alpha(self.canvas, center_x - self.star_size, center_y - self.star_size,
                                                center_x + self.star_size, center_y + self.star_size,
                                                fill="#8B451380")  # Dark brown with 50% opacity

        # Add speckled texture to the star
        self.speckles = []  # List to store speckles

    def animate_sideways_motion(self):
        # Determine current shift speed based on whether we're in the burst phase
        current_time = time.time()
        shift_distance = self.initial_burst_speed if current_time < self.burst_end_time else self.speckle_shift_distance

        # Move each speckle rightward by the shift distance
        for speckle in self.speckles:
            # Shift the speckle to the right
            self.canvas.move(speckle, shift_distance, 0)

            # Get the current position of the speckle
            x1, _, x2, _ = self.canvas.coords(speckle)

            # Check if the speckle has moved out of the star's area
            if x2 > self.canvas.winfo_width():
                # Delete the speckle
                self.canvas.delete(speckle)
                self.speckles.remove(speckle)

        # Schedule the next animation frame
        self.root.after(50, self.animate_sideways_motion)

    def generate_new_speckle(self):
        # Determine current generation interval based on whether we're in the burst phase
        current_time = time.time()
        generation_interval = self.initial_burst_generation_interval if current_time < self.burst_end_time else self.speckle_generation_interval

        # Generate a new speckle off-screen to the left
        speckle_x = -50  # Ensure it spawns off-screen to the left
        speckle_y = random.uniform(0, self.canvas.winfo_height())  # Random y position within the canvas height
        shade = random.randint(0, 0)
        speckle_color = "#{:02x}{:02x}{:02x}".format(shade, shade, shade)
        speckle_radius = random.uniform(1, 1)
        new_speckle = create_oval_with_alpha(self.canvas, speckle_x - speckle_radius, speckle_y - speckle_radius,
                                             speckle_x + speckle_radius, speckle_y + speckle_radius, fill=speckle_color)
        self.speckles.append(new_speckle)  # Add the speckle to the list

        # Schedule the next speckle generation
        self.root.after(generation_interval, self.generate_new_speckle)

    def star_base_right_boundary(self):
        return self.star_center_x + self.star_size

    def animate_hue_shift(self):
        hue_shift = math.sin(self.time * self.hue_shift_speed) * self.hue_shift_factor

        # Update the hue of the star base
        r, g, b, _ = hex_to_rgb_and_alpha("#8B451380")  # Dark brown base color
        new_r = min(255, max(0, int(r + hue_shift)))  # Ensure new value is within [0, 255]
        new_g = min(255, max(0, int(g + hue_shift)))
        new_b = min(255, max(0, int(b + hue_shift)))
        new_color = "#{:02x}{:02x}{:02x}".format(new_r, new_g, new_b)

        self.canvas.itemconfig(self.star_base, fill=new_color)

        # Increment time for hue shifting
        self.time += 0.05

        # Schedule the next animation frame
        self.root.after(50, self.animate_hue_shift)

if __name__ == "__main__":
    root = tk.Tk()
    app = StarSystemViewer(root)
    root.mainloop()
