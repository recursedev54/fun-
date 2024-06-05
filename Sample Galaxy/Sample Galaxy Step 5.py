import tkinter as tk
from tkinter import simpledialog  # Import simpledialog explicitly
import random
import json

class SampleGalaxyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sample Galaxy")
        
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.star_systems = []  # List to store created star systems
        self.load_star_systems()  # Load star systems from JSON file
        self.create_galaxy_view()

    def create_galaxy_view(self):
        # Clear canvas and destroy existing buttons
        self.canvas.delete("all")
        self.destroy_buttons()

        # Display the galaxy visualization (basic circle for now)
        self.canvas.create_oval(100, 100, 700, 500, outline="white", width=2)

        # Redraw existing star systems if they exist
        for system in self.star_systems:
            self.draw_star_system(system)

        # Button to create a new star system
        self.create_system_button = tk.Button(self.root, text="Create Star System", command=self.create_star_system)
        self.create_system_button.pack()

    def draw_star_system(self, system):
        # Draw a star system representation
        x, y = system['coords']  # Get coordinates of the star system
        oval = self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="yellow")

        # Tag binding to handle clicks on the oval representing the star system
        self.canvas.tag_bind(oval, "<Button-1>", lambda event, system=system: self.view_star_system(system))

    def create_star_system(self):
        # Generate random coordinates for the new star system
        x = random.randint(150, 650)
        y = random.randint(150, 450)

        # Generate a random 6-digit hex code for the star system name
        system_name = '#' + ''.join(random.choices('0123456789abcdef', k=6))

        # Draw a star system representation
        star_system = {'coords': (x, y), 'name': system_name}
        self.star_systems.append(star_system)
        self.save_star_systems()  # Save star systems to JSON file

        # Redraw the galaxy view
        self.create_galaxy_view()

    def delete_star_system(self, system):
        # Remove the star system from the list
        self.star_systems.remove(system)
        self.save_star_systems()  # Save star systems to JSON file

        # Return to the galaxy view
        self.create_galaxy_view()

    def rename_star_system(self, system):
        # Prompt the user for a new name for the star system
        new_name = simpledialog.askstring("Rename Star System", "Enter a new name for the star system:")

        if new_name:
            # Update the name of the star system
            system['name'] = new_name
            self.save_star_systems()  # Save star systems to JSON file

            # Redraw the galaxy view
            self.create_galaxy_view()

    def load_star_systems(self):
        try:
            with open("star_systems.json", "r") as file:
                self.star_systems = json.load(file)
        except FileNotFoundError:
            self.star_systems = []

    def save_star_systems(self):
        with open("star_systems.json", "w") as file:
            json.dump(self.star_systems, file)

    def destroy_buttons(self):
        # Destroy existing buttons
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

    def view_star_system(self, system):
        # Clear canvas and destroy existing buttons
        self.canvas.delete("all")
        self.destroy_buttons()

        # Placeholder for viewing the star system
        # For now, let's just redraw the galaxy and a label indicating the current star system
        self.canvas.create_oval(100, 100, 700, 500, outline="white", width=2)
        name = system.get('name', f"Star System {self.star_systems.index(system) + 1}")
        self.canvas.create_text(400, 50, text=name, fill="white", font=("Arial", 16, "bold"))

        # Button to add a file to the star system
        self.add_file_button = tk.Button(self.root, text="Add File", command=lambda: self.add_file(system))
        self.add_file_button.pack()

        # Button to listen to audio files in the star system
        self.listen_button = tk.Button(self.root, text="Listen to Audio", command=lambda: self.listen_to_audio(system))
        self.listen_button.pack()

        # Button to return to the galaxy view
        self.return_button = tk.Button(self.root, text="Return to Galaxy", command=self.create_galaxy_view)
        self.return_button.pack()

        # Button to delete the star system
        self.delete_button = tk.Button(self.root, text="Delete", command=lambda: self.delete_star_system(system))
        self.delete_button.pack()

        # Button to rename the star system
        self.rename_button = tk.Button(self.root, text="Rename", command=lambda: self.rename_star_system(system))
        self.rename_button.pack()

    def add_file(self, system):
        # Placeholder for adding a file to the star system
        print(f"File added to star system {system['name']}")

   
    def listen_to_audio(self, system):
        # Placeholder for listening to audio files in the star system
        print(f"Listening to audio files in star system {system['name']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SampleGalaxyApp(root)
    root.mainloop()

