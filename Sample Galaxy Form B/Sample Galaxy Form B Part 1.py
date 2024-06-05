import tkinter as tk

class StarSystemViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Star System Viewer")
        
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        # Draw the star
        self.draw_star()

    def draw_star(self):
        # Draw a simple star in the center of the canvas
        star_size = 80
        star_color = "yellow"
        center_x, center_y = 400, 300
        self.star = self.canvas.create_oval(center_x - star_size, center_y - star_size,
                                             center_x + star_size, center_y + star_size,
                                             fill=star_color, outline="")

if __name__ == "__main__":
    root = tk.Tk()
    app = StarSystemViewer(root)
    root.mainloop()
