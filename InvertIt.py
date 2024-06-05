import cv2

# Function to invert colors of an image
def invert_colors(frame):
    return cv2.bitwise_not(frame)

# Open video capture
cap = cv2.VideoCapture('sentiment_video.mp4')

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error: Couldn't open video file")
    exit()

# Get the frames per second (fps) of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the width and height of the video frames
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a VideoWriter object to write the inverted video
out = cv2.VideoWriter('inverted_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()

    # Check if frame is successfully read
    if not ret:
        break

    # Invert colors of the frame
    inverted_frame = invert_colors(frame)

    # Write the inverted frame to the output video
    out.write(inverted_frame)

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()
