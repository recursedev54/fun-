import tkinter as tk
from tkinter import ttk
import pygame
import threading
import time

class RadioPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Radio Player")

        self.frequency_label = tk.Label(master, text="Frequency:")
        self.frequency_label.pack()

        self.frequency_scale = ttk.Scale(master, from_=87.5, to=108.0, length=300, orient="horizontal")
        self.frequency_scale.pack()

        self.frequency_display = tk.Label(master, text="")
        self.frequency_display.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.pack(pady=5)

        pygame.mixer.init()

        self.radio_thread = None
        self.is_playing = False

    def play(self):
        if self.is_playing:
            self.stop()
        else:
            frequency = self.frequency_scale.get()
            self.frequency_display.config(text=f"Playing: {frequency} MHz")
            self.radio_thread = threading.Thread(target=self.play_radio, args=(frequency,))
            self.radio_thread.start()

    def stop(self):
        self.is_playing = False
        pygame.mixer.music.stop()
        if self.radio_thread and self.radio_thread.is_alive():
            self.radio_thread.join()

    def play_radio(self, frequency):
        self.is_playing = True
        audio_file = f"audio_files/{frequency}.mp3"  # Assuming audio files are named after frequencies
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() and self.is_playing:
            time.sleep(0.1)

if __name__ == "__main__":
    root = tk.Tk()
    app = RadioPlayer(root)
    root.mainloop()
