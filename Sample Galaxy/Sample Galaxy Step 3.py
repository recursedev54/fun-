import tkinter as tk
import random
import pygame.mixer

class SampleGalaxyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sample Galaxy")
        
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.star_systems = []  # List to store created star systems
        self.total_star_systems = 0  # Variable to track the total number of star systems created

        self.create_galaxy_view()

    def create_galaxy_view(self):
        # Clear canvas and destroy existing buttons
        self.canvas.delete("all")
        self.destroy_buttons()

    # Display the galaxy visualization (basic circle for now)
        self.canvas.create_oval(100, 100, 700, 500, outline="white", width=2)

    # Redraw existing star systems if they exist
        for system in self.star_systems:
            if self.canvas.type(system) == "oval":
                self.draw_star_system(system)

    # Button to create a new star system
        self.create_system_button = tk.Button(self.root, text="Create Star System", command=self.create_star_system)
        self.create_system_button.pack()


    def draw_star_system(self, system):
        # Placeholder for drawing a star system
        # For now, let's just draw a yellow circle representing the star system
        x, y = self.canvas.coords(system)[:2]  # Get coordinates of the star system
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="yellow")

    def create_star_system(self):
        # Generate random coordinates for the new star system
        x = random.randint(150, 650)
        y = random.randint(150, 450)

        # Draw a star system representation
        star_system = self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="yellow")
        self.star_systems.append(star_system)
        self.total_star_systems += 1

        # Bind click event to the star system
        self.canvas.tag_bind(star_system, "<Button-1>", lambda event, system=star_system: self.view_star_system(system))

    def view_star_system(self, system):
        # Clear canvas and destroy existing buttons
        self.canvas.delete("all")
        self.destroy_buttons()

        # Placeholder for viewing the star system
        # For now, let's just redraw the galaxy and a label indicating the current star system
        self.canvas.create_oval(100, 100, 700, 500, outline="white", width=2)
        self.canvas.create_text(400, 50, text=f"Star System {self.star_systems.index(system) + 1}", fill="white", font=("Arial", 16, "bold"))

        # Button to add a file to the star system
        self.add_file_button = tk.Button(self.root, text="Add File", command=lambda: self.add_file(system))
        self.add_file_button.pack()

        # Button to listen to audio files in the star system
        self.listen_button = tk.Button(self.root, text="Listen to Audio", command=lambda: self.listen_to_audio(system))
        self.listen_button.pack()

        # Button to return to the galaxy view
        self.return_button = tk.Button(self.root, text="Return to Galaxy", command=self.create_galaxy_view)
        self.return_button.pack()

    def add_file(self, system):
        # Placeholder for adding a file to the star system
        print(f"File added to star system {self.star_systems.index(system) + 1}")

    def listen_to_audio(self, system):
        # Placeholder for listening to audio files in the star system
        print(f"Listening to audio files in star system {self.star_systems.index(system) + 1}")

    def destroy_buttons(self):
        # Destroy existing buttons
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SampleGalaxyApp(root)
    root.mainloop()
