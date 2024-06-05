import aubio
import numpy as np

def audio_to_text(audio_path):
    # Create a pitch object
    samplerate = 44100
    hop_size = 512
    pitch_o = aubio.pitch("default", 2048, hop_size, samplerate)

    # Open the audio file
    print("Opening audio file:", audio_path)
    try:
        audio_source = aubio.source(audio_path, samplerate, hop_size)
    except FileNotFoundError:
        return "Audio file not found"

    # Process the audio file
    print("Processing audio file...")
    while True:
        audio_data, _ = audio_source()
        if len(audio_data) < hop_size:
            break
        pitch = pitch_o(audio_data.astype(np.float32))[0]
        print("Pitch:", pitch)
        if pitch != 0.0:
            print("Pitch detected. Breaking out of loop.")
            break

    # Check if a pitch was detected
    if pitch == 0.0:
        return "No pitch detected"

    text = f"The detected pitch is {pitch:.2f} Hz"

    return text

# Path to your audio file
audio_path = "C:\\Users\\zreba\\Downloads\\crows snippit.wav"

# Convert audio to text with additional context
transcribed_text = audio_to_text(audio_path)
print("Transcribed Text:")
print(transcribed_text)
