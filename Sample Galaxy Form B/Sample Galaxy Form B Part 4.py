import tkinter as tk
import random
import time

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b)

def create_oval(canvas, x1, y1, x2, y2, fill):
    color = f'#{fill}'
    oval = canvas.create_oval(x1, y1, x2, y2, fill=color, outline="")
    return oval

class StarSystemViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Star System Viewer")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.web_generation_interval = 20  # Interval in milliseconds to generate new web
        self.web_shift_distance = -2  # Reverse direction: move webs leftward in each iteration

        self.initial_quick_speed = 10  # Speed during the initial quick phase
        self.initial_quick_generation_interval = 200  # Generation interval during the initial quick phase
        self.initial_quick_duration = 3  # Duration of the initial quick phase in seconds
        self.quick_active = False  # Flag to track if quick phase is active
        self.quick_end_time = None  # Variable to store the end time of quick phase

        # Generate and animate webs
        self.generate_new_web()  # Start generating webs continuously
        self.animate_sideways_motion()  # Call the sideways motion animation for webs
        self.start_quick()  # Start the quick phase

    def generate_new_web(self):
        # Generate a new web off-screen to the right
        web_x = self.canvas.winfo_width() + 50  # Ensure it spawns off-screen to the right
        web_y = random.uniform(0, self.canvas.winfo_height())  # Random y position within the canvas height
        shade = random.randint(0, 255)
        web_color = "{:02x}{:02x}{:02x}".format(shade, shade, shade)
        web_radius = random.uniform(1, 1)
        create_oval(self.canvas, web_x - web_radius, web_y - web_radius,
                    web_x + web_radius, web_y + web_radius, fill=web_color)

        # Schedule the next web generation
        self.root.after(self.web_generation_interval, self.generate_new_web)

    def animate_sideways_motion(self):
        # Move each web leftward by the shift distance
        for web in self.canvas.find_all():
            # Shift the web to the left
            self.canvas.move(web, self.web_shift_distance, 0)

            # Get the current position of the web
            x1, _, x2, _ = self.canvas.coords(web)

            # Check if the web has moved out of the canvas
            if x2 < 0:
                # Delete the web
                self.canvas.delete(web)

        # Schedule the next animation frame
        self.root.after(50, self.animate_sideways_motion)

    def start_quick(self):
        self.quick_active = True
        self.quick_end_time = time.time() + self.initial_quick_duration
        self.root.after(0, self.generate_quick_webs)

    def generate_quick_webs(self):
        if not self.quick_active:
            return

        # Generate a quick of webs
        for _ in range(50):
            web_x = random.uniform(0, self.canvas.winfo_width())
            web_y = random.uniform(0, self.canvas.winfo_height())
            shade = random.randint(0, 255)
            web_color = "{:02x}{:02x}{:02x}".format(shade, shade, shade)
            web_radius = random.uniform(1, 1)
            create_oval(self.canvas, web_x - web_radius, web_y - web_radius,
                        web_x + web_radius, web_y + web_radius, fill=web_color)

        # Schedule next quick generation if quick phase is still active
        if time.time() < self.quick_end_time:
            self.root.after(self.initial_quick_generation_interval, self.generate_quick_webs)
        else:
            self.quick_active = False

if __name__ == "__main__":
    root = tk.Tk()
    app = StarSystemViewer(root)
    root.mainloop()
