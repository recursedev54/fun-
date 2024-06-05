import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Colored Text Display")

# Define a function to display colored text
def display_colored_text(text, x, y, color):
    font = pygame.font.SysFont(None, 40)  # Use default system font, size 40
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Main loop
def main():
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(WHITE)

        # Display colored text with RGB color values
        display_colored_text("Hello, World!", 100, 100, (255, 0, 0))  # Red
        display_colored_text("This is colored text.", 100, 150, (0, 255, 0))  # Green
        display_colored_text("Custom RGB color.", 100, 200, (0, 0, 255))  # Blue

        # Update the display
        pygame.display.update()

# Run the main function
if __name__ == "__main__":
    main()
