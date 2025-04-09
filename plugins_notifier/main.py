from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from plugins_loader import load_plugins

app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app, cors_allowed_origins="*")
notifiers = load_plugins(socketio=socketio)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/test_notify")
def test_notify():
    socketio.emit("notify", {"title": "测试", "message": "来自真实运行实例的通知"}, namespace="/")
    return "ok"


@app.route('/send_notify', methods=['POST'])
def send_notify():
    data = request.json
    title = data.get('title', '测试标题')
    message = data.get('message', '测试消息')

    for notifier in notifiers:
        notifier.notify(title, message)

    return jsonify({"status": "ok", "notifiers": [n.name for n in notifiers]})


if __name__ == '__main__':
    socketio.run(app, port=5001, debug=True)
