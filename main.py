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

<<<<<<< HEAD
print("make conflict")
=======
print('화이팅 지윤님')
>>>>>>> 6c7f2bd0bbcd424c09152c34e829676b55f024c6
