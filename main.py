from rtmbot import RtmBot
from rtmbot.core import Plugin
import secret

from select import select_chat_girl, select_topic, select_agile

class RandomChat(Plugin):
    def process_message(self, data):
        print(data)
        if "잡담" in data["text"]:
            girl = select_chat_girl()
            topic = select_topic()
            talk = "오늘은 *" + girl + "* 과 함께 *"+ topic + "* 에 대해 대화를 나눠보세요"
            self.outputs.append([data["channel"], talk])
        elif "애자일" in data["text"]:
            agile = select_agile()
            self.outputs.append([data["channel"], agile])

config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.RandomChat"]
}
bot = RtmBot(config)
bot.start()


# print("make conflict")
# print('화이팅 지윤님')
