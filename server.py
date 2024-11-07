"""
Flask web application for emotion detection using Watson NLP.
Provides an endpoint to analyze emotions in a given text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Endpoint to analyze the emotions of the provided text.
    
    Retrieves the 'textToAnalyze' query parameter, sends it to the emotion detection function,
    and returns a response with the emotion analysis. If the input text is invalid, it returns
    an error message.

    Returns:
        str: Formatted string with emotion scores, or an error message if input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze', '').strip()
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is 'anger': {response.get('anger', 0)}, "
        f"'disgust': {response.get('disgust', 0)}, 'fear': {response.get('fear', 0)}, "
        f"'joy': {response.get('joy', 0)}, 'sadness': {response.get('sadness', 0)}. "
        f"The dominant emotion is {response.get('dominant_emotion', 'unknown')}."
    )

    return response_text

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the application.

    Returns:
        str: The rendered HTML content of index.html.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
