import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, simpledialog
import json

class ColorPaletteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Color Palette Manager")

        self.palettes = []

        self.canvas = tk.Canvas(self.master, width=500, height=500)  # Adjusted height here
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.canvas.yview, takefocus=False)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.frame, anchor=tk.NW)

        self.create_button = tk.Button(self.master, text="Create Palette", command=self.create_palette)
        self.save_button = tk.Button(self.master, text="Save Palette", command=self.save_palette)
        self.load_button = tk.Button(self.master, text="Load Palette", command=self.load_palette)

        self.create_button.pack()
        self.save_button.pack()
        self.load_button.pack()

        # Create edit and delete buttons
        self.edit_button = tk.Button(self.master, text="Edit Palette", command=self.edit_selected_palette)
        self.delete_button = tk.Button(self.master, text="Delete Palette", command=self.delete_selected_palette)
        self.edit_button.pack()
        self.delete_button.pack()

    def create_palette(self):
        colors = []
        palette_name = simpledialog.askstring("Name Palette", "Enter palette name:")
        if palette_name:
            while True:
                color_option = messagebox.askquestion("Color Option", "Do you want to pick a color from the picker?")
                if color_option == 'yes':
                    color = colorchooser.askcolor()[1]
                else:
                    color_hex = simpledialog.askstring("Enter Color", "Enter color hex code (e.g., #RRGGBB):")
                    if color_hex is None:
                        break  # If the user cancels, exit the loop
                    color_hex = color_hex.strip()  # Remove any leading/trailing whitespace
                    if color_hex.startswith('#') and len(color_hex) == 7:
                        try:
                            int(color_hex[1:], 16)  # Check if it's a valid hexadecimal color code
                        except ValueError:
                            messagebox.showerror("Invalid Color", "Please enter a valid hexadecimal color code.")
                            continue
                        else:
                            color = color_hex
                    else:
                        messagebox.showerror("Invalid Color", "Please enter a valid hexadecimal color code.")
                        continue
                if color is None:
                    break
                colors.append(color)
                if len(colors) >= 10 or not messagebox.askyesno("Add More Colors", "Do you want to add more colors?"):
                    break
            if colors:
                self.palettes.append({"name": palette_name, "colors": colors})
                self.display_loaded_palettes()  # Call the method to display the newly created palette

    def edit_selected_palette(self):
        if not self.palettes:
            messagebox.showwarning("No Palettes", "No palettes to edit.")
            return

        edit_window = tk.Toplevel(self.master)
        edit_window.title("Select Palette to Edit")

        tk.Label(edit_window, text="Select a palette:").pack()

        listbox = tk.Listbox(edit_window)
        listbox.pack(fill=tk.BOTH, expand=True)

        for palette in self.palettes:
            listbox.insert(tk.END, palette["name"])

        def edit_palette():
            selected_index = listbox.curselection()
            if selected_index:
                selected_palette = self.palettes[selected_index[0]]
                self.edit_palette_colors(selected_palette)
                edit_window.destroy()
            else:
                messagebox.showwarning("No Selection", "Please select a palette to edit.")

        tk.Button(edit_window, text="Edit", command=edit_palette).pack()

    def delete_selected_palette(self):
        if not self.palettes:
            messagebox.showwarning("No Palettes", "No palettes to delete.")
            return

        delete_window = tk.Toplevel(self.master)
        delete_window.title("Select Palette to Delete")

        tk.Label(delete_window, text="Select a palette:").pack()

        listbox = tk.Listbox(delete_window)
        listbox.pack(fill=tk.BOTH, expand=True)

        for palette in self.palettes:
            listbox.insert(tk.END, palette["name"])

        def delete_palette():
            selected_index = listbox.curselection()
            if selected_index:
                selected_palette_name = self.palettes[selected_index[0]]["name"]
                self.palettes.pop(selected_index[0])
                self.display_loaded_palettes()
                delete_window.destroy()
                messagebox.showinfo("Deleted", f"Palette '{selected_palette_name}' deleted successfully.")
            else:
                messagebox.showwarning("No Selection", "Please select a palette to delete.")

        tk.Button(delete_window, text="Delete", command=delete_palette).pack()

    def edit_palette_colors(self, palette):
        edit_window = tk.Toplevel(self.master)
        edit_window.title(f"Edit Palette - {palette['name']}")
        
        rows = len(palette["colors"])
        color_entries = []

        def add_color_entry():
            color_entry = tk.Entry(edit_window, width=10)
            color_entry.grid(row=len(color_entries), column=0, columnspan=2)
            color_entries.append(color_entry)

        def delete_color_entry():
            if len(color_entries) > 0:
                if messagebox.askyesno("Delete Color", "Are you sure you want to delete the last color?"):
                    color_entries[-1].destroy()
                    color_entries.pop()

        for i, color in enumerate(palette["colors"]):
            tk.Label(edit_window, text=f"Color {i+1}:", width=10).grid(row=i, column=0)
            color_entry = tk.Entry(edit_window, width=10)
            color_entry.insert(0, color)
            color_entry.grid(row=i, column=1)
            color_entries.append(color_entry)

        tk.Button(edit_window, text="Add Color", command=add_color_entry).grid(row=rows, column=0)
        tk.Button(edit_window, text="Delete Color", command=delete_color_entry).grid(row=rows, column=1)

        def save_changes():
            palette["colors"] = [entry.get() for entry in color_entries]
            edit_window.destroy()
            self.display_loaded_palettes()

        tk.Button(edit_window, text="Save", command=save_changes).grid(row=rows+1, column=0, columnspan=2)

    def display_palette(self, name, colors, y_offset):
        x, y = 50, y_offset
        self.canvas.create_text(x - 25, y + 10, text=name, tags=("palette_name", name))  # Add tags for identification
        for i, color in enumerate(colors):
            self.canvas.create_rectangle(x, y, x + 50, y + 50, fill=color)
            self.canvas.create_text(x + 25, y + 60, text=color)
            x += 60

    def display_loaded_palettes(self):
        # Clear the canvas before redrawing
        self.canvas.delete("all")

        self.frame.destroy()
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.frame, anchor=tk.NW)

        y_offset = 10  # Initial vertical offset
        for palette in self.palettes:
            self.display_palette(palette["name"], palette["colors"], y_offset)
            y_offset += 100  # Increment the vertical offset for the next palette

        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def save_palette(self):
        if not self.palettes:
            messagebox.showwarning("No Palette", "Create a palette first.")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".json")
        if filename:
            with open(filename, "w") as f:
                json.dump(self.palettes, f)
            messagebox.showinfo("Success", "Palette saved successfully.")

    def load_palette(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filename:
            with open(filename, "r") as f:
                loaded_palettes = json.load(f)
            self.palettes = loaded_palettes
            self.display_loaded_palettes()

def main():
    root = tk.Tk()
    app = ColorPaletteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
