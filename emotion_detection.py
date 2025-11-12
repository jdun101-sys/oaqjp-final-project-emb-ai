import requests

def emotion_detector(text_to_analyze):
    # URL of the emotion dectector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Custom header specifying the model ID for the emotion dectector service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}    
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the emotion dectector API
    response = requests.post(url, json=myobj, headers=header)

    # Returning text containing emotion dectector results
    return response.text
