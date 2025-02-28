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
        extra_headers={
            # Optional. Site URL for rankings on openrouter.ai.
            "HTTP-Referer": "<YOUR_SITE_URL>",
            # Optional. Site title for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>",
        },
        extra_body={},
        model="deepseek/deepseek-r1-distill-llama-70b:free",
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
