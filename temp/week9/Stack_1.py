def isStackFull():
    global stack, top, SIZE
    if(top >= SIZE-1):
        return True
    else:
        return False
def isStackEmpty():
    global stack, top, SIZE
    if(top == -1):
        return True
    else:
        return False

#추가/제거 코드
def Push(data):
    global stack, top, SIZE
    if(isStackFull()):
        print("Stack Full")
        return
    top += 1
    stack[top] = data
def Pop():
    global stack, top, SIZE
    if(isStackEmpty()):
        print("Stack Empty")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data
def Peek():
    global stack, top, SIZE
    if(isStackEmpty()):
        print("Stack Empty")
        return None
    return stack[top]

#초기값 초기화
SIZE = 2
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    while True:
        print(stack)
        inder = int(input("데이터 추가:1, 데이터 제거:2, 데이터 찾기:3, 종료:4--> "))
        if inder == 1:
            if(isStackFull()):
                print("Stack Full\n")
                continue
            data = input("입력할 데이터 입력-->")
            Push(data)
        elif inder == 2:
            data = Pop()
        elif inder == 3:
            Peek()
        elif inder == 4:
            print("종료하겠습니다")
            break
        else:
            print("잘못된 입력입니다.\n")
            continue
