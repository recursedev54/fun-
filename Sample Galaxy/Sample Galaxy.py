import tkinter as tk

class SampleGalaxyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sample Galaxy")
        
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.create_galaxy_view()

    def create_galaxy_view(self):
        # Display the galaxy visualization (basic circle for now)
        self.canvas.create_oval(100, 100, 700, 500, outline="white", width=2)

        # Button to create a new star system
        self.create_system_button = tk.Button(self.root, text="Create Star System", command=self.create_star_system)
        self.create_system_button.pack()

    def create_star_system(self):
        # Placeholder for creating a new star system
        print("New star system created!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SampleGalaxyApp(root)
    root.mainloop()
