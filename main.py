from rtmbot import RtmBot
from rtmbot.core import Plugin
import secret
from random import randint

class RandomChat(Plugin):
    def process_message(self, data):
        if "잡담" in data["text"]:
            girl = select_chat_girl()
            topic = select_topic()
            talk = "오늘은 *" + girl + "* 과 함께 *"+ topic + "* 에 대해 대화를 나눠보세요"
            self.outputs.append([data["channel"], talk])

girls =['지영', '희영', '예빈', '다솜', '지윤']
topics = ['연애', '취미', '좋아하는 예능', '좋아하는 동물', '버킷리스트',
'로또가 된다면 뭘 할까?', '이상형', '좋아하는 계절', '이대로 멈췄으면, 했던 순간',
'최고의 여행지', '영화', '3년안에 꼭 해보고 싶은 것', '데잇걸즈 끝나고 뭐하고싶은지']

def select_chat_girl():
    len_girls = len(girls)
    girl = girls[randint(0, len_girls)]
    return girl

def select_topic():
    len_topic = len(topics)
    topic = topics[randint(0, len_topic)]
    return topic

config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.RandomChat"]
}
bot = RtmBot(config)
bot.start()


# print("make conflict")
# print('화이팅 지윤님')
