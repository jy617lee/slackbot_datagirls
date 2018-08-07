from rtmbot import RtmBot
from rtmbot.core import Plugin
import secret


class StartReview(Plugin):
    def process_message(self, data):
        print(data)
config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": []
}
bot = RtmBot(config)
bot.start()

def process_message(self, data):
    if "안녕" in data["text"]:
        self.outputs.append([data["channel"], "오늘 하루도 수고많았어. 오늘은 어땠어?"])

print('화이팅 지윤님')
print('나의 수정수정 수정이다')
print("make conflict")
