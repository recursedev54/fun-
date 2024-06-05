import json
import random
import math
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon if not already done
nltk.download('vader_lexicon')

# Initialize the sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

def preprocess_corpus(corpus):
    """Preprocess the corpus text."""
    return corpus.lower().replace('"','').replace("'",'').replace('\n','').replace(')','').replace('(','').replace('[','').replace(']','').replace('’','').replace("“",'').replace("”",'')

def shannon_entropy(word_counts):
    """Calculate Shannon entropy."""
    total_count = sum(word_counts.values())
    entropy = 0
    for count in word_counts.values():
        probability = count / total_count
        entropy -= probability * math.log2(probability)
    return entropy

def adjust_probabilities(word_probabilities, sentiment_score, sentiment_weight=1.0):
    """Adjust word probabilities based on sentiment score."""
    adjusted_probabilities = {}
    for word, probability in word_probabilities.items():
        word_sentiment = sid.polarity_scores(word)['compound']
        adjustment = sentiment_score['compound'] * word_sentiment * sentiment_weight
        adjusted_probabilities[word] = probability * (1 + adjustment)
    # Normalize probabilities
    total_probability = sum(adjusted_probabilities.values())
    for word in adjusted_probabilities:
        adjusted_probabilities[word] /= total_probability
    return adjusted_probabilities

def generate_response(user_input, ngram, window_size, sentiment_weight=1.0):
    """Generate a response based on the user input and the n-gram model."""
    out = ''
    
    # Combine user input and base corpus
    combined_corpus = user_input + ' ' + corpus
    
    # Preprocess combined corpus
    combined_corpus = preprocess_corpus(combined_corpus)
    
    # Split combined corpus into tokens
    tokens = combined_corpus.split()
    
    # Populate n-gram from combined corpus
    for i in range(len(tokens) - window_size):
        word_pair = tuple(tokens[i:i+window_size])
        if '' in word_pair:
            continue
        next_word = tokens[i+window_size]
        ngram.setdefault(word_pair, []).append(next_word)
    
    # Calculate Shannon entropy for each word pair
    entropy_scores = {}
    for word_pair, next_words in ngram.items():
        next_word_counts = {}
        for word in next_words:
            next_word_counts[word] = next_word_counts.get(word, 0) + 1
        entropy_scores[word_pair] = shannon_entropy(next_word_counts)
    
    # Sort word pairs by entropy in descending order
    sorted_word_pairs = sorted(entropy_scores, key=entropy_scores.get, reverse=True)
    
    # Get the word pairs with the highest entropy
    high_entropy_word_pairs = sorted_word_pairs[:10]
    
    # Choose a word pair from the high entropy word pairs
    chosen_word_pair = random.choice(high_entropy_word_pairs)
    
    # Mirror the user's input length
    out = ' '.join(chosen_word_pair)
    
    # Get sentiment score of the input
    sentiment_score = sid.polarity_scores(user_input)
    print(f"Input Sentiment: {sentiment_score}")

    while len(out.split()) < len(user_input.split()):
        if chosen_word_pair not in ngram.keys():
            break
        next_word_options = ngram[chosen_word_pair]
        
        # Calculate word probabilities
        next_word_counts = {word: next_word_options.count(word) for word in set(next_word_options)}
        total_counts = sum(next_word_counts.values())
        word_probabilities = {word: count / total_counts for word, count in next_word_counts.items()}
        
        # Adjust word probabilities based on sentiment score
        adjusted_probabilities = adjust_probabilities(word_probabilities, sentiment_score, sentiment_weight)
        
        # Choose the next word based on adjusted probabilities
        next_word = random.choices(list(adjusted_probabilities.keys()), weights=adjusted_probabilities.values(), k=1)[0]
        
        out += ' ' + next_word
        chosen_word_pair = (chosen_word_pair[1], next_word)
    
    # Print sentiment of the generated output
    output_sentiment = sid.polarity_scores(out)
    print(f"Output Sentiment: {output_sentiment}")
    
    return out

# Load corpus from text file
with open('codeyxxxsama.txt', 'r', encoding='utf-8') as file:
    corpus = file.read()

# Preprocess the corpus text
corpus = preprocess_corpus(corpus)


ngram = {}
window_size = 2  # Adjust window size as needed

# Main loop for interactive chat
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    
    # Generate response
    response = generate_response(user_input, ngram, window_size, sentiment_weight=2.0)  # Increased sentiment weight for stronger effect
    print('Bot:', response)
