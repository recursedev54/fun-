import math
import re
import pygame
import sys
from collections import Counter

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Colored Text Display")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define a function to display colored text
def display_colored_text(text, x, y, color):
    font = pygame.font.SysFont(None, 40)  # Use default system font, size 40
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def count_syllables(word):
    # A very basic syllable counter
    return max(1, len(re.findall(r'[aeiouy]+', word, re.IGNORECASE)))

def shannon_entropy(text):
    # Count the occurrences of each character in the text
    freqs = Counter(text)
    # Calculate the probability of each character
    probs = [float(freq) / len(text) for freq in freqs.values()]
    # Calculate Shannon entropy
    entropy = -sum(p * math.log2(p) for p in probs)
    return entropy

def renyi_entropy(text, alpha):
    # Count the occurrences of each character in the text
    freqs = Counter(text)
    # Calculate the probability of each character
    probs = [float(freq) / len(text) for freq in freqs.values()]
    # Calculate Rényi entropy
    entropy = 1 / (1 - alpha) * math.log2(sum(p**alpha for p in probs))
    return entropy

def generate_rgb_code(entropy):
    # Extract the digits after the decimal point
    digits = str(entropy - int(entropy))[2:8]
    # Generate RGB code
    rgb_code = tuple(int(digits[i:i+2], 16) for i in range(0, 6, 2))
    return rgb_code

def colorize_text(sentence):
    # Split the sentence into words
    words = sentence.split()
    x, y = 50, 50
    for i in range(len(words) - 1):
        # Check if the word pair is one syllable
        if count_syllables(words[i]) == 1 and count_syllables(words[i + 1]) == 1:
            # Calculate Shannon entropy for the pair
            pair_entropy_shannon = shannon_entropy(words[i] + " " + words[i + 1])
            # Calculate Rényi entropy for the pair
            pair_entropy_renyi = renyi_entropy(words[i] + " " + words[i + 1], alpha=16)
            # Generate RGB code from entropy
            rgb_code = generate_rgb_code(pair_entropy_renyi)
            # Apply the color to the word pair and add to colored text
            display_colored_text(words[i] + " " + words[i + 1], x, y, rgb_code)
            y += 50
        else:
            # If the word pair is not one syllable, simply append both words
            display_colored_text(words[i] + " " + words[i + 1], x, y, BLACK)
            y += 50
    # Add the last word if it's a single syllable
    if count_syllables(words[-1]) == 1:
        display_colored_text(words[-1], x, y, BLACK)

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

        # Create entry widget for input sentence
        entry = input("Enter a sentence: ")

        # Generate colored text
        colorize_text(entry)

        # Update the display
        pygame.display.update()

# Run the main function
if __name__ == "__main__":
    main()
