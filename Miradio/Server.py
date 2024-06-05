from flask import Flask, send_file

app = Flask(__name__)

# Define routes for each radio stream URL
@app.route("/<frequency>")
def play_station(frequency):
    # You need to implement logic to map frequency to audio files
    # Here we're just returning different audio files based on the frequency
    if frequency == "87.5":
        return send_file("Moon Jelly.wav")
    elif frequency == "88.0":
        return send_file("8ball.wav")
    # Add more routes for other frequencies as needed...
    else:
        return "Frequency not found"

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
