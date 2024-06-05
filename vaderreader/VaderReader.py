import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure the VADER lexicon is downloaded
nltk.download('vader_lexicon')

def analyze_sentiment(file_path):
    # Initialize the VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Open the file and read lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Analyze and print the sentiment for each line
    for idx, line in enumerate(lines, start=1):
        # Skip empty or whitespace-only lines
        if not line.strip():
            continue
        
        sentiment_scores = sid.polarity_scores(line)
        print(f"Line {idx}: {line.strip()}")
        print(f"Sentiment: {sentiment_scores}")
        print("")

# Replace 'your_file.txt' with the path to your text file
file_path = 'DeadLinesHostile.txt'
analyze_sentiment(file_path)
