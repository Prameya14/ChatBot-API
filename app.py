from flask import Flask, request
# from g4f.client import Client
from markdown import markdown
from openai import OpenAI

app = Flask(__name__)


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    response = markdown(get_Chat_response(input))
    return response


def get_Chat_response(text):
    # client = Client()
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}]
    # )

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=True)
