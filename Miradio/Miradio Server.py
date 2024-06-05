from flask import Flask, send_file

app = Flask(__name__)

# Define routes for each radio stream URL
@app.route("/station1")
def station1():
    return send_file("Moon Jelly.wav")

@app.route("/station2")
def station2():
    return send_file("8ball.wav")

# Add more routes for other stations as needed...

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode
