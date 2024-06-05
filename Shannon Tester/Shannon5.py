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
    print("Digits:", digits)  # Debug print
    # Generate RGB code if digits are not empty
    if digits and len(digits) >= 6:
        rgb_code = tuple(int(digits[i:i+2], 16) for i in range(0, 6, 2))
    else:
        rgb_code = (0, 0, 0)  # Default to black if no valid digits
    return rgb_code

def colorize_text(sentence):
    # Split the sentence into words
    words = sentence.split()
    x, y = 50, 50
    for i in range(len(words)):
        # Calculate entropy for the current word
        word_entropy = shannon_entropy(words[i])
        print("Entropy for '{}': {}".format(words[i], word_entropy))  # Debug print
        rgb_code = generate_rgb_code(word_entropy)
        display_colored_text(words[i], x, y, rgb_code)
        y += 50

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
