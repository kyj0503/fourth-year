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
def checkBracket(expr):
    for ch in expr:
        if ch in '([{<':
            Push(ch)
        elif ch in ')]}>':
            out = Pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else: return False
        else: pass
    if isStackEmpty(): return True
    else: return False

#초기값 초기화
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    exprAry = ['(A+B)', ')A+B(', '((A+B-C', '(A+B]', '(<A+{B-C}/[C*D]>)']
    for expr in exprAry:
        top = -1
        print(expr, '==>', checkBracket(expr))