import tkinter as tk
import random

class SampleGalaxyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sample Galaxy")
        
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.star_systems = []  # List to store created star systems

        self.create_galaxy_view()

    def create_galaxy_view(self):
        # Display the galaxy visualization (basic circle for now)
        self.canvas.create_oval(100, 100, 700, 500, outline="white", width=2)

        # Button to create a new star system
        self.create_system_button = tk.Button(self.root, text="Create Star System", command=self.create_star_system)
        self.create_system_button.pack()

    def create_star_system(self):
        # Generate random coordinates for the new star system
        x = random.randint(150, 650)
        y = random.randint(150, 450)

        # Draw a star system representation
        star_system = self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="yellow")
        self.star_systems.append(star_system)

        # Bind click event to the star system
        self.canvas.tag_bind(star_system, "<Button-1>", lambda event, system=star_system: self.view_star_system(system))

    def view_star_system(self, system):
        # Placeholder for viewing the star system
        print(f"Viewing star system {system}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SampleGalaxyApp(root)
    root.mainloop()
