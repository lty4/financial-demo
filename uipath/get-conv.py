import requests

def get_conversation(id):
    conversation_id = id

    """Setup Rasa API to get conversation information"""
    rasa_url = "http://35.224.230.180/core"
    rasa_token = "i0MDjoixPrsISPX"
    rasa_conversation_api_url = rasa_url + "/conversations/" + conversation_id + "/tracker?token=" + rasa_token

    """Get the conversation"""
    rasa_conversation = requests.get(url=rasa_conversation_api_url)

    return rasa_conversation.json()