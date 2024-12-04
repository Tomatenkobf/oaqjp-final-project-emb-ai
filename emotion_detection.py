import json
import requests

def emotion_detector(text_to_analyze):
    #Definition of the API URL:
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #Create a Payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Make a POST request to the API with the payload and headers
    response = requests.post(URL, json=myobj, headers=header)
    # Parse the response from the API
    formatted_response = json.loads(response.text)
    # If the response status code is 200, extract the data
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]["emotion"]["anger"]
        disgust_score = formatted_response['emotionPredictions'][0]["emotion"]['disgust']
        fear_score = formatted_response['emotionPredictions'][0]["emotion"]['fear']
        joy_score = formatted_response['emotionPredictions'][0]["emotion"]['joy']
        sadness_score = formatted_response['emotionPredictions'][0]["emotion"]['sadness']
    # If the response status code is 500, set data to none
    elif response.status_code == 500:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None

    #create dictionary
    emotion_dict = {'anger': anger_score,
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score, 
                    }
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    emotion_dict['dominant_emotion'] = dominant_emotion

    # Return the dictionary
    return emotion_dict