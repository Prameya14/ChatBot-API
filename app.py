from flask import Flask, request
from g4f.client import Client
from markdown import markdown

app = Flask(__name__)


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    response = markdown(get_Chat_response(input))
    return response


def get_Chat_response(text):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=True)
