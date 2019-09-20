from monkeylearn import MonkeyLearn
import json 

try:
    from .sentiment_analysis_config import API_KEY_MONKEYLEARN
except:
    API_KEY_MONKEYLEARN = ''

def request_sentiment(message):
    data = [message]
    ml = MonkeyLearn(API_KEY_MONKEYLEARN)
    model_id = 'cl_pi3C7JiL'
    result = ml.classifiers.classify(model_id, data)
    #result_json = json.loads(result.body)
    sentiment = result.body[0]['classifications'][0]['tag_name']
    return sentiment
