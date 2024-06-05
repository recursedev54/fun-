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
    for i, word in enumerate(words):
        if word in processed_words:  # Skip if word already processed as part of a pair
            continue
        if len(word) > 5:
            # For long words, calculate Rényi entropy individually
            word_entropy = renyi_entropy(word, alpha=16)
            rgb_code = generate_rgb_code(word_entropy)
            display_colored_text(word, x, y, rgb_code)
            y += 50
            processed_words.add(word)  # Mark word as processed
        elif i == len(words) - 1:
            # For the last word, calculate Rényi entropy
            word_entropy = renyi_entropy(word, alpha=16)
            rgb_code = generate_rgb_code(word_entropy)
            display_colored_text(word, x, y, rgb_code)
            y += 50
        else:
            # For short words, combine them into pairs
            word_pair = word + ' ' + words[i + 1]
            pair_entropy = renyi_entropy(word_pair, alpha=16)
            rgb_code = generate_rgb_code(pair_entropy)
            display_colored_text(word_pair, x, y, rgb_code)
            y += 50
            processed_words.add(word)  # Mark first word of pair as processed
            processed_words.add(words[i + 1])  # Mark second word of pair as processed

# Function to draw text input box
def draw_text_input_box():
    pygame.draw.rect(screen, WHITE, (50, 500, 700, 50))  # Draw input box
    pygame.draw.rect(screen, BLACK, (50, 500, 700, 50), 2)  # Draw border

def main():
    sentence = ""
    input_active = True
    while True:
        screen.fill(WHITE)  # Clear the screen
        draw_text_input_box()  # Draw text input box
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        sentence = sentence[:-1]
                    else:
                        sentence += event.unicode

        if not input_active:
            colorize_text(sentence)  # Generate colored text
        else:
            font = pygame.font.SysFont(None, 40)  # Use default system font, size 40
            rendered_text = font.render(sentence, True, BLACK)
            screen.blit(rendered_text, (55, 510))

        pygame.display.update()

if __name__ == "__main__":
    main()
