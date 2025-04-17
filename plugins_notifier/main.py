import os
import sys


def _add_root_path():
    # 添加项目根目录（code_tools）到 sys.path，os.pardir 表示上级目录（..）
    PROJECT_ROOT = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)


# 在导入其他模块前执行
_add_root_path()

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
