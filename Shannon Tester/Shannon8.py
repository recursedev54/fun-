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
    processed_words = set()  # Keep track of processed words
    for i in range(len(words)):
        if words[i] in processed_words:  # Skip if word already processed as part of pair
            continue
        # Consider long words as individual pairs
        if len(words[i]) > 5:
            word_entropy = renyi_entropy(words[i], alpha=16)  # Calculate Rényi entropy
            print("Entropy for '{}': {}".format(words[i], word_entropy))  # Debug print
            rgb_code = generate_rgb_code(word_entropy)
            display_colored_text(words[i], x, y, rgb_code)
            y += 50
            processed_words.add(words[i])  # Mark word as processed
        else:
            # Combine short words into pairs
            if i < len(words) - 1:
                word_pair = words[i] + ' ' + words[i + 1]
                pair_entropy = renyi_entropy(word_pair, alpha=16)  # Calculate Rényi entropy for pair
                print("Entropy for '{}': {}".format(word_pair, pair_entropy))  # Debug print
                rgb_code = generate_rgb_code(pair_entropy)
                display_colored_text(word_pair, x, y, rgb_code)
                y += 50
                processed_words.add(words[i])  # Mark first word of pair as processed
                processed_words.add(words[i + 1])  # Mark second word of pair as processed

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
