import math
from collections import Counter

def shannon_entropy(text):
    # Count the occurrences of each character in the text
    char_count = Counter(text)
    
    # Total number of characters in the text
    total_chars = len(text)
    
    # Calculate the probability of each character
    probabilities = [char_count[char] / total_chars for char in char_count]
    
    # Calculate Shannon entropy
    entropy = -sum(p * math.log2(p) for p in probabilities)
    
    return entropy

def main():
    while True:
        text = input("Enter the text (press Enter to exit): ")
        if not text:
            break
        entropy = shannon_entropy(text)
        print("Shannon Entropy:", entropy)

if __name__ == "__main__":
    main()
