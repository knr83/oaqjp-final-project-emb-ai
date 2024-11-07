import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    # Check if text_to_analyze is blank
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    try:
        # Send POST request
        response = requests.post(url, json=payload, headers=headers)
        
        # Handle response for blank entries (status code 400)
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        response.raise_for_status()  # Raise an error for other HTTP issues

        # Process JSON response
        res = response.json()
        if 'emotionPredictions' in res and res['emotionPredictions']:
            emotions = res['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)
            emotions['dominant_emotion'] = dominant_emotion
            return emotions

        # Return None if 'emotionPredictions' is not in response
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
