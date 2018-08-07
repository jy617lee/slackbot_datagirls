from random import randint
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
