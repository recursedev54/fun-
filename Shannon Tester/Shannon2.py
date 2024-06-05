import math
from collections import Counter

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
    if alpha == 1:
        return shannon_entropy(text)
    else:
        entropy = 1 / (1 - alpha) * math.log2(sum(p**alpha for p in probs))
        return entropy

while True:
    text = input("Enter a string of text (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        break

    print("Shannon Entropy:", shannon_entropy(text))

    alpha = float(input("Enter the value of alpha for Rényi entropy calculation: "))
    print("Rényi Entropy (α={}):".format(alpha), renyi_entropy(text, alpha))
