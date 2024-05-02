import random

# 이 리스트에는 무작위 응답이 들어 있습니다. (원하는 대로 추가하거나 번역해도 됩니다)
random_responses = ["아주 흥미로운데, 더 자세히 말해 주세요.",
                    "그렇군요. 계속 이야기해 주세요.",
                    "왜 그런 말씀을 하시는 거죠?",
                    "요즘 날씨가 정말 재미있죠, 그렇죠?",
                    "주제를 바꾸죠.",
                    "어젯밤 경기를 보셨나요?"]

print("안녕하세요, 나는 간단한 로봇 Marvin입니다.")
print("‘bye’를 입력하여 언제든 대화를 종료할 수 있습니다.")
print("각 답변을 입력한 후 '엔터' 키를 누르세요.")
print("오늘 기분은 어떠세요?")

while True:
    # 사용자가 텍스트를 입력할 때까지 기다립니다.
    user_input = input("> ")
    if user_input.lower() == "bye":
        # 사용자가 'bye'를 입력하면 (또는 BYE, ByE, byE 등), 루프를 탈출합니다.
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("대화해 주셔서 감사합니다. 안녕히 가세요!")
