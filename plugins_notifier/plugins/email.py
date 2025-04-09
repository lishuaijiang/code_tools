from email.mime.text import MIMEText
from plugins_notifier.plugins import NotifierBase
import smtplib


class EmailNotifier(NotifierBase):
    name = "Email"

    def notify(self, title, message):
        sender = "sender@example.com"
        receiver = "receiver@example.com"
        password = "your-smtp-password"

        msg = MIMEText(message, "plain", "utf-8")
        msg["Subject"] = title
        msg["From"] = sender
        msg["To"] = receiver

        try:
            """
            注意配置 DNS
                nameserver 114.114.114.114
                nameserver 8.8.8.8
            """
            smtp = smtplib.SMTP("smtp.qq.com", 587)
            # smtp = smtplib.SMTP("183.47.101.192", 587)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(sender, password)
            smtp.sendmail(sender, [receiver], msg.as_string())
            smtp.quit()
            print("📧 邮件通知已发送")
        except Exception as e:
            print("❌ 邮件发送失败:", e)
