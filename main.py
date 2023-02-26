# 引入必要的库
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# 创建一个 Flask 应用程序
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# 创建路由，提供前端界面
@app.route('/')
def index():
    return render_template('index.html')

# 处理客户端连接和断开
@socketio.on('connect')
def handle_connect():
    print('客户端已连接')

@socketio.on('disconnect')
def handle_disconnect():
    print('客户端已断开连接')

# 监听来自客户端的消息，并将其广播到所有其他连接的客户端
@socketio.on('message')
def handle_message(message):
    print('接收到消息：', message)
    emit('message', message, broadcast=True)

# 启动服务器
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
