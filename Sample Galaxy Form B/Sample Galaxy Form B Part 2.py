import tkinter as tk
import random
import math
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

class StarSystemViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Star System Viewer")
        
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()
        
        self.time = 0  # Time counter for hue shifting effect
        self.hue_shift_speed = 6  # Speed of hue shifting
        self.hue_shift_factor = 4  # Hue shift factor

        self.draw_star()
        self.animate_hue_shift()

    def draw_star(self):
        center_x, center_y = 400, 300
        star_size = 80

        # Draw the star base
        self.star_base = create_oval_with_alpha(self.canvas, center_x - star_size, center_y - star_size,
                                                center_x + star_size, center_y + star_size,
                                                fill="#8B451380")  # Dark brown with 50% opacity

    def animate_hue_shift(self):
        hue_shift = math.sin(self.time * self.hue_shift_speed) * self.hue_shift_factor

        # Update the hue of the star base
        r, g, b, _ = hex_to_rgb_and_alpha("#8B451380")  # Dark brown base color
        new_r = min(255, max(0, int(r + hue_shift)))  # Ensure new value is within [0, 255]
        new_g = min(255, max(0, int(g + hue_shift)))
        new_b = min(255, max(0, int(b + hue_shift)))
        new_color = "#{:02x}{:02x}{:02x}".format(new_r, new_g, new_b)
        #print("New Color:", new_color)  # Debug output

        self.canvas.itemconfig(self.star_base, fill=new_color)

        # Increment time for hue shifting
        self.time += 0.05

        # Schedule the next animation frame
        self.root.after(50, self.animate_hue_shift)







if __name__ == "__main__":
    root = tk.Tk()
    app = StarSystemViewer(root)
    root.mainloop()
