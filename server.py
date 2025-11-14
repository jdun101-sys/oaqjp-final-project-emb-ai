"""
Flask server with routes for rendering the index page and returning emotion
detection results based on user-submitted text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    '''
    This endpoint returns index.html file
    '''
    # Return index.html
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    '''
    This endpoint returns the results from the emotion detector function
    based on the text to analyze.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion in the response is None
    if response["dominant_emotion"] is None:
        # Return text to instruct the user to try again with valid input
        return "Invalid text! Please try again!"

    # Format the reponse to be displayed
    response_text = f"For the given statement, the system response is 'anger': \
    {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, \
    'joy': {response['joy']}, and 'sadness': {response['sadness']}. The dominant emotion is \
    {response['dominant_emotion']}."

    # Return emotion detector text
    return response_text

if __name__ == "__main__":
    app.run(debug=True, port=5000)
