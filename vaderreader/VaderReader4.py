import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import cv2
import numpy as np

# Ensure the VADER lexicon is downloaded
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

def analyze_sentiment(file_path):
    # Open the file and read lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Store timestamps, sentiment scores, and hex codes
    timestamps = []
    hex_codes_list = []

    # Gather timestamps and sentiment scores for each line
    for idx, line in enumerate(lines, start=1):
        # Skip empty or whitespace-only lines
        if not line.strip():
            continue
        
        # Prompt user for timestamp
        timestamp = input(f"Enter timestamp for Line {idx}: ")
        timestamps.append(float(timestamp))
        
        sentiment_scores = sid.polarity_scores(line)
        
        # Convert sentiment scores to RGB values
        neg_rgb = int(sentiment_scores['neg'] * 255)
        neu_rgb = int(sentiment_scores['neu'] * 255)
        pos_rgb = int(sentiment_scores['pos'] * 255)
        
        # Convert RGB values to hexadecimal
        hex_code = "#{:02x}{:02x}{:02x}".format(neg_rgb, neu_rgb, pos_rgb)
        hex_codes_list.append(hex_code)

    print("Timestamps:", timestamps)
    print("Hex Codes:", hex_codes_list)

    print("Number of timestamps:", len(timestamps))

    # Define video properties
    width, height = 800, 600
    fps = 24
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter('sentiment_video2.mp4', fourcc, fps, (width, height))

    # Create frames for video
    for i in range(len(timestamps) - 1):
        start_time = timestamps[i]
        end_time = timestamps[i + 1]
        start_color = hex_codes_list[i]
        end_color = hex_codes_list[i + 1]

        while start_time < end_time:
            # Check if the current time is within 0.5 seconds of a timestamp
            if start_time - timestamps[i] <= 0.5:
                color = hex_to_rgb(start_color)
            elif end_time - start_time <= 0.5:
                color = hex_to_rgb(end_color)
            else:
                color = [1, 1, 1]  # Default to white

            # Create frame with the determined color
            frame = np.full((height, width, 3), color, dtype=np.uint8)
            
            # Write frame to video
            video_writer.write(frame)

            # Update start time
            start_time += 1 / fps

    # Release video writer
    video_writer.release()

def hex_to_rgb(hex_code):
    # Convert hex code to RGB values
    r = int(hex_code[1:3], 16)
    g = int(hex_code[3:5], 16)
    b = int(hex_code[5:], 16)
    return [b, g, r]  # Return in BGR format for OpenCV

# Replace 'your_file.txt' with the path to your text file
file_path = 'DeadlinesHostile.txt'
analyze_sentiment(file_path)
