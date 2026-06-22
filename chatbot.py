import json
import random
from textblob import TextBlob

with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def get_response(user_message):

    user_message = user_message.lower()

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            if pattern.lower() in user_message:

                return random.choice(
                    intent["responses"]
                )

    return "Sorry, I didn't understand your question."


def analyze_sentiment(text):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"

    elif polarity < 0:
        return "Negative"

    return "Neutral"