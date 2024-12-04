''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the data from the response
    response_dict = {"anger": response['anger'],
                    "disgust": response['disgust'],
                    "fear": response['fear'],
                    "joy": response['joy'],
                    "sadness": response['sadness'],
                    "dominant_emotion": response['dominant_emotion']}

    # Check if an error or invalid input ocurred
    if response_dict["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    else:
        # Exclude the 'dominant_emotion' key
        emotions = {k: v for k, v in response_dict.items() if k != 'dominant_emotion'}

        # Create a list of formatted emotion strings
        emotion_strings = [f"'{k}': {v}" for k, v in emotions.items()]

        # Join the emotion strings with commas and 'and' before the last item
        if len(emotion_strings) > 1:
            emotions_text = ', '.join(emotion_strings[:-1]) + ' and ' + emotion_strings[-1]
        else:
            emotions_text = emotion_strings[0]

        # Construct and print the final output
        return "For the given statement, the system response is {}. The dominant emotion is {}.".format(emotions_text, response_dict['dominant_emotion']
)


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug="on")
