import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion dectector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Custom header specifying the model ID for the emotion dectector service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}    
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the emotion dectector API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotions which contains anger, disgust, fear,
    # joy and sadness from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Finding the dominant emotion with the highest score
    dominant_emotion = max(emotions, key=emotions.get)

    # Adding dominant emotion to emotions object
    emotions["dominant_emotion"] = dominant_emotion
    
    # Returning json containing emotion dectector results
    return emotions
