from flask import Flask, render_template
from flask_socketio import SocketIO
import openai

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
openai.api_key = 'your-api-key'

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=150
    )
    emit('reply', response.choices[0].text)

if __name__ == '__main__':
    socketio.run(app, debug=True)
