'''Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_analyzer():
    '''Analyze the emotion of the text provided in the request arguments.

    Returns:
        str: A string containing the emotions detected and the dominant emotion.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the data from the response
    response_dict = {
        "anger": response['anger'],
        "disgust": response['disgust'],
        "fear": response['fear'],
        "joy": response['joy'],
        "sadness": response['sadness'],
        "dominant_emotion": response['dominant_emotion']
    }

    # Check if an error or invalid input occurred
    if response_dict["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Exclude the 'dominant_emotion' key
    emotions = {
        k: v for k, v in response_dict.items() if k != 'dominant_emotion'
    }

    # Create a list of formatted emotion strings
    emotion_strings = [f"'{k}': {v}" for k, v in emotions.items()]

    # Join the emotion strings with commas and 'and' before the last item
    if len(emotion_strings) > 1:
        emotions_text = ', '.join(emotion_strings[:-1]) + ' and ' + emotion_strings[-1]
    else:
        emotions_text = emotion_strings[0]

    # Construct and return the final output
    return (
        f"For the given statement, the system response is {emotions_text}. "
        f"The dominant emotion is {response_dict['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    '''Render the index page.'''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
