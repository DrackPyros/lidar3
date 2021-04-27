from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')
@socketio.on('my event')
def my_event(msg):
    print (msg['data'])
@socketio.on('connect')

def on_connect():
    emit('rsp', {'status':'Conectado'})
    
@socketio.on('disconnect')
def disconnect():
    print ('Desconectado')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')