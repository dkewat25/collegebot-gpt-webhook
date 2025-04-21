from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Get API key from environment or hardcode for testing
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    user_query = req['queryResult']['queryText']

    # GPT response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful college assistant."},
            {"role": "user", "content": user_query}
        ]
    )

    gpt_reply = response['choices'][0]['message']['content']

    return jsonify({"fulfillmentText": gpt_reply})

if __name__ == '__main__':
    app.run()
