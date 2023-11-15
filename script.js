const protocol = (window.location.protocol === 'https:') ? 'wss://' : 'ws://';
const socket = io.connect(protocol + window.location.host);

document.getElementById('send-button').addEventListener('click', function() {
    const message = document.getElementById('chat-input').value;
    socket.emit('message', message);
    addMessageToChatBox('You: ' + message);
    document.getElementById('chat-input').value = '';
});

socket.on('reply', function(data) {
    addMessageToChatBox('Support: ' + data);
});

function addMessageToChatBox(message) {
    const chatBox = document.getElementById('chat-box');
    const newMessage = document.createElement('div');
    newMessage.textContent = message;
    chatBox.appendChild(newMessage);
}
