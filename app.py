import chat

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userInput = request.args.get('msg')
    return str(chat.get_response(userInput))

if __name__ == "__main__":
    app.run()