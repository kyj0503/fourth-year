# 스택 선언
SIZE = 100  # 스택의 최대 크기
stack = [None for _ in range(SIZE)]  # 스택을 리스트로 구현
top = -1  # top은 스택의 가장 위를 가리키는 인덱스, -1이면 비어있는 상태

# 스택이 비었는지 확인하는 함수
def isStackEmpty():
    global top
    return top == -1  # top이 -1이면 스택이 비어있음

# 스택이 꽉 찼는지 확인하는 함수
def isStackFull():
    global top
    return top >= SIZE - 1  # top이 마지막 인덱스 이상이면 스택이 가득 참

# 스택에 데이터를 삽입하는 함수
def push(item):
    global top
    if isStackFull():  # 스택이 가득 차면 더 이상 삽입할 수 없음
        print("스택이 꽉 찼습니다.")
        return
    top += 1  # top 위치 증가 후
    stack[top] = item  # 해당 위치에 데이터 삽입

# 스택에서 데이터를 꺼내는 함수
def pop():
    global top
    if isStackEmpty():  # 스택이 비어있으면 꺼낼 수 없음
        print("스택이 비었습니다.")
        return None
    item = stack[top]  # 가장 위에 있는 데이터를 꺼냄
    top -= 1  # top 위치 감소
    return item

# 회문을 검사하는 함수
def checkPalindrome(text):
    global top
    top = -1  # 검사 전에 스택 초기화

    text = text.replace(" ", "")  # 공백 제거 (공백을 무시한 회문 검사)

    # 문자열의 각 문자를 스택에 삽입
    for ch in text:
        push(ch)

    # 스택에서 문자를 하나씩 꺼내어 역순 문자열을 만듦
    reversedText = ''
    while not isStackEmpty():
        reversedText += pop()

    # 원래 문자열과 역순 문자열을 비교
    return text == reversedText

# 메인 실행 루프
if __name__ == "__main__":
    while True:
        # 사용자로부터 입력 받기
        inputStr = input("문장을 입력해주세요(x 입력시 종료): ")
        if inputStr == 'x':  # 'x' 입력 시 종료
            break

        print("입력한 문장 :", inputStr)
        print("회문을 검사합니다.\n")

        # 회문 여부 검사 및 출력
        if checkPalindrome(inputStr):
            print(f"문장: '{inputStr}'은/는 회문입니다.\n")
        else:
            print(f"문장: '{inputStr}'은/는 회문이 아닙니다.\n")
