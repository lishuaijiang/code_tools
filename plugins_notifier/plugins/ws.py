from plugins_notifier.plugins import NotifierBase


class WebSocketNotifier(NotifierBase):
    name = "WebSocket"

    def __init__(self, socketio):
        # 防止导入的 socketio 和主进程的 socketio 不是同一个
        self.socketio = socketio

    def notify(self, title, message):
        self.socketio.emit('notify', {'title': title, 'message': message}, namespace="/")
        print("🛰️WebSocket 已发送")
