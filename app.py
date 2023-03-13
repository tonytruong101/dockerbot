from flask import Flask, render_template, request
import openai
import re

app = Flask(__name__)

def is_code(message):
    regex = r"^FROM[\s\S]*$"
    return re.match(regex, message)

class Message:
    def __init__(self, content, position):
        self.content = content
        self.position = position

messages = []

openai.api_key = "" # replace with your actual OpenAI API key

# Define the format_response function
def format_response(response):
    if response.startswith("```") and response.endswith("```"):
        return response  # Already formatted, return as is
    elif is_code(response):
        return "```\n{}\n```".format(response)
    else:
        return "```\n{}\n```".format(response.strip())

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/result', methods=['POST'])
def result():
    user_input = request.form.get('user_input')
    messages.append(Message(user_input, 'right'))

    # Get bot response from OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="The user said: {}\nThe bot responded:".format(user_input),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    bot_response = response.choices[0].text.strip()
    formatted_response = format_response(bot_response)  # Format the response
    messages.append(Message(formatted_response, 'left'))

    return index()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6001)

