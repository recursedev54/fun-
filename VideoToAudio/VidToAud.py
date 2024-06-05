import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def video_to_audio(video_path, audio_path):
    # Load the video file
    video = VideoFileClip(video_path)
    
    # Extract the audio
    audio = video.audio
    
    # Write the audio to a file
    audio.write_audiofile(audio_path)

def select_video_file():
    # Open a file dialog to select the video file
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.mkv;*.avi;*.mov")])
    if video_path:
        # Suggest an audio file name based on the video file name
        audio_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if audio_path:
            video_to_audio(video_path, audio_path)
            print(f"Audio file saved as: {audio_path}")

# Create a simple GUI
root = tk.Tk()
root.title("Video to Audio Converter")

btn = tk.Button(root, text="Select Video File", command=select_video_file)
btn.pack(pady=20)

root.mainloop()
