import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time  # Import the time module

# Placeholder for lyrics corpus (new line indicates a new timestamp)
lyrics_corpus = """
Hello, it's me
I was wondering
"""

# Placeholder for timestamps in seconds (each line corresponds to the lyrics above)
timestamps_corpus = """
0
2
"""

# Process the lyrics and timestamps
lyrics = lyrics_corpus.strip().split('\n')
timestamps = [float(t.split(':')[0]) * 60 + float(t.split(':')[1]) if ':' in t else float(t) for t in timestamps_corpus.strip().split('\n')]

# Initialize plot
fig, ax = plt.subplots()
ax.axis('off')  # Hide axes
text = ax.text(0.5, 0.5, '', fontsize=15, ha='center', va='center', wrap=True)

# Update function for the animation
def update(frame):
    if frame < len(lyrics):
        text.set_text(lyrics[frame])
    return text,

# Create the animation
def run_animation():
    start_time = time.time()
    for i, timestamp in enumerate(timestamps):
        elapsed_time = time.time() - start_time
        while elapsed_time < timestamp:
            elapsed_time = time.time() - start_time
        update(i)
        plt.draw()
        plt.pause(0.01)  # Pause briefly to allow for screen update

run_animation()
plt.show()
