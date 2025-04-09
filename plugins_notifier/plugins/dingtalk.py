from plugins_notifier.plugins import NotifierBase
import requests


class DingTalkNotifier(NotifierBase):
    name = "dingtalk"

    def notify(self, title, message):
        """未测试，T2群未解散"""
        webhook = "https://oapi.dingtalk.com/robot/send?access_token=<KEY>"
        payload = {
            "msgtype": "text",
            "text": {"content": f"{title} - {message}"}
        }
        try:
            res = requests.post(webhook, json=payload)
            print("🤖 钉钉返回:", res.text)
        except Exception as e:
            print("❌ 钉钉发送失败:", e)
