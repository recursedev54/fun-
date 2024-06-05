import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import cv2
import numpy as np

# Ensure the VADER lexicon is downloaded
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

def convert_to_seconds(timestamp_str):
    # Check if the timestamp string is in the format 'm:ss'
    if re.match(r'\d+:\d+', timestamp_str):
        minutes, seconds = map(int, timestamp_str.split(':'))
        return minutes * 60 + seconds
    # Check if the timestamp string is just seconds
    elif re.match(r'\d+', timestamp_str):
        return int(timestamp_str)
    else:
        raise ValueError("Invalid timestamp format. Please use 'm:ss' or 'ss'.")

def analyze_sentiment(file_path):
    # Open the file and read lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Store timestamps, sentiment scores, and hex codes
    timestamps = []
    hex_codes_list = []

    # Gather timestamps and sentiment scores for each line
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        # Print the line number and the line itself
        print(f"Line {idx + 1}: {line.strip()}")

        # Skip empty or whitespace-only lines
        if not line.strip():
            idx += 1
            continue
        
        # Prompt user for timestamp
        timestamp_str = input(f"Enter timestamp for Line {idx + 1} (e.g., 1:25 or 75): ")
        if timestamp_str.lower() == "back" and idx > 0:
            idx -= 1
            continue

        try:
            timestamp_seconds = convert_to_seconds(timestamp_str)
            timestamps.append(timestamp_seconds)
            
            sentiment_scores = sid.polarity_scores(line)
            
            # Convert sentiment scores to RGB values
            neg_rgb = int(sentiment_scores['neg'] * 255)
            neu_rgb = int(sentiment_scores['neu'] * 255)
            pos_rgb = int(sentiment_scores['pos'] * 255)
            
            # Convert RGB values to hexadecimal
            hex_code = "#{:02x}{:02x}{:02x}".format(neg_rgb, neu_rgb, pos_rgb)
            hex_codes_list.append(hex_code)

            idx += 1
        except ValueError as e:
            print(e)

    print("Timestamps:", timestamps)
    print("Hex Codes:", hex_codes_list)

    print("Number of timestamps:", len(timestamps))

    # Define video properties
    width, height = 800, 600
    fps = 24
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter('sentiment_video.mp4', fourcc, fps, (width, height))

    # Create frames for video
    for i in range(len(timestamps) - 1):
        start_time = timestamps[i]
        end_time = timestamps[i + 1]
        start_color = hex_codes_list[i]
        end_color = hex_codes_list[i + 1]

        while start_time < end_time:
            # Interpolate colors
            t_rel = (start_time - timestamps[i]) / (timestamps[i + 1] - timestamps[i])
            r = int(start_color[1:3], 16) + t_rel * (int(end_color[1:3], 16) - int(start_color[1:3], 16))
            g = int(start_color[3:5], 16) + t_rel * (int(end_color[3:5], 16) - int(start_color[3:5], 16))
            b = int(start_color[5:], 16) + t_rel * (int(end_color[5:], 16) - int(start_color[5:], 16))

            # Create frame with interpolated color
            frame = np.full((height, width, 3), (b, g, r), dtype=np.uint8)
            
            # Write frame to video
            video_writer.write(frame)

            # Update start time
            start_time += 1 / fps

    # Release video writer
    video_writer.release()

# Replace 'your_file.txt' with the path to your text file
file_path = 'DeadlinesHostile.txt'
analyze_sentiment(file_path)
