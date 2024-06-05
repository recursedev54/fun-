import tkinter as tk

def hex_to_rgb(hex_color):
    """Convert hexadecimal color code to RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    """Convert RGB color to hexadecimal."""
    return '#%02x%02x%02x' % rgb_color

def tritan_simulation(hex_color):
    """Simulate Tritanopia by shifting blue and green components."""
    # Convert hexadecimal color to RGB
    rgb_color = hex_to_rgb(hex_color)

    # Calculate the shift ratio
    ratio = [0, 0]
    if rgb_color[0] != 0:
        ratio[0] = rgb_color[0] / 255.0
    if rgb_color[2] != 255:
        ratio[1] = (255 - rgb_color[2]) / 255.0

    # Adjust green and blue components
    new_color1 = (int(128 * ratio[0]), rgb_color[1], int(128 * ratio[1]))
    new_color2 = (rgb_color[0], int(128 + (127 * ratio[1])), int(128 - (128 * ratio[0])))

    # Convert RGB colors back to hexadecimal
    hex_color1 = rgb_to_hex(new_color1)
    hex_color2 = rgb_to_hex(new_color2)

    return hex_color1, hex_color2

def simulate():
    """Callback function to simulate Tritanopia and display results."""
    input_color = entry.get()
    try:
        hex_color1, hex_color2 = tritan_simulation(input_color)
        label_color1.config(bg=hex_color1)
        label_color2.config(bg=hex_color2)
        label_hex1.config(text=hex_color1)
        label_hex2.config(text=hex_color2)
    except ValueError:
        label_color1.config(bg="white")
        label_color2.config(bg="white")
        label_hex1.config(text="")
        label_hex2.config(text="")

# GUI Setup
root = tk.Tk()
root.title("Tritan Simulator")

label_input = tk.Label(root, text="Input Hex Color:")
label_input.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

button_simulate = tk.Button(root, text="Simulate", command=simulate)
button_simulate.grid(row=0, column=2)

label_color1 = tk.Label(root, text="Color 1", width=10, height=5)
label_color1.grid(row=1, column=0)

label_color2 = tk.Label(root, text="Color 2", width=10, height=5)
label_color2.grid(row=1, column=1)

label_hex1 = tk.Label(root, text="", bg="white")
label_hex1.grid(row=2, column=0)

label_hex2 = tk.Label(root, text="", bg="white")
label_hex2.grid(row=2, column=1)

root.mainloop()
