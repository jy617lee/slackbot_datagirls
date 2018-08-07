from random import randint
girls =['지영', '희영', '예빈', '다솜', '지윤']
topics = ['연애', '취미', '좋아하는 예능', '좋아하는 동물', '버킷리스트',
'로또가 된다면 뭘 할까?', '이상형', '좋아하는 계절', '이대로 멈췄으면, 했던 순간',
'최고의 여행지', '영화', '3년안에 꼭 해보고 싶은 것', '데잇걸즈 끝나고 뭐하고싶은지']

agiles = [
'우리가 풀려는 문제를 사람들이 가지고 있고 해결하기 위해 얼마나 노력하고 있나요?',
'A/B 테스트는 우리 비지니스에 가장 핵심이 되는 것을 고르자',
'돈 내고 쓸 만큼 좋은 것인가요?',
'팀원들과의 신뢰는 모든 것의 첫걸음!!',
'나이, 성별은 올바른 타겟을 특정하기 힘든 경우도 많아요',
'사람은 자율성, 역량, 소속감을 가져야 동기가 생긴대요. 우리 모두는 동기가 충분한가요?',
'새로운 정보가 추가되지 않는다면, 하나의 문제에 대해 15분 이상 이야기하지 않는게 좋아요',
'오늘은 팀원 중 가장 오래 개인적으로 얘기하지 않은 사람과 이야기해보세요'
]
def select_chat_girl():
    len_girls = len(girls)
    girl = girls[randint(0, len_girls)]
    return girl

def select_topic():
    len_topic = len(topics)
    topic = topics[randint(0, len_topic)]
    return topic

def select_agile():
    len_agile = len(agiles)
    agile = agiles[randint(0, len_agile)]
    return agile
