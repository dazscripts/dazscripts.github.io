from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

import openai


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

app.config['SECRET_KEY'] = 'secret!'
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=message,
        max_tokens=150
    )
    emit('reply', response.choices[0].text)

if __name__ == '__main__':
    socketio.run(app, debug=True)

