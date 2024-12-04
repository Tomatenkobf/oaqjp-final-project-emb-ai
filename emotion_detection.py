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
    return response.text