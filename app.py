from flask import Flask, render_template, request

app = Flask(__name__)

class Message:
    def __init__(self, content, position):
        self.content = content
        self.position = position

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/result', methods=['POST'])
def result():
    user_input = request.form.get('user_input')
    messages.append(Message(user_input, 'right'))
    # TODO: Implement bot response
    messages.append(Message('This is a response from the bot', 'left'))
    return index()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6001)

