from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from chatbot import get_response
from chatbot import analyze_sentiment

from database import (
    init_db,
    save_chat,
    get_all_chats,
    get_chat_count
)

app = Flask(__name__)

init_db()


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data["message"]

    bot_response = get_response(
        user_message
    )

    sentiment = analyze_sentiment(
        user_message
    )

    save_chat(
        user_message,
        bot_response,
        sentiment
    )

    return jsonify({
        "response": bot_response,
        "sentiment": sentiment
    })


@app.route("/admin")
def admin():

    chats = get_all_chats()

    total_chats = get_chat_count()

    return render_template(
        "admin.html",
        chats=chats,
        total_chats=total_chats
    )


if __name__ == "__main__":
    app.run(debug=True)