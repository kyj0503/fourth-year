## 함수 선언 부분 ##
class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


## 전역 변수 선언 부분 ##
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인 코드 부분 ##
if __name__ == "__main__":
    node = TreeNode()
    node.data = nameAry[0]
    root = node
    memory.append(node)

    for name in nameAry[1:]:
        node = TreeNode()
        node.data = name
        current = root
        while True:
            if name < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right
        memory.append(node)
    print("이진 탐색 트리 구성 완료!")

    findName = '마마무'

    current = root
    parent = None
    while True:
        if findName == current.data: # 단어 발견시 곧바로 break
            print(findName, '을(를) 찾음')
            break
        elif findName < current.data: # 단어를 왼쪽부터 탐색
            if current.left == None:
                print(findName, '이(가) 트리에 없음')
                break
            print("노드를 왼쪽 서브트리로 이동합니다.")
            current = current.left
        else: # 왼쪽에서 탐색한 이후에, 단어를 오른쪽에서 탐색
            if current.right == None:
                print(findName, '이(가) 트리에 없음')
                break
            print("노드를 오른쪽 서브트리로 이동합니다.")
            current = current.right

