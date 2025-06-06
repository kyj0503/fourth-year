class Node():
    def __init__(self):
        self.data = None # 데이터 저장
        self.link = None # 다음 노드를 가리키는 포인터

# 연결 리스트를 돌면서 모든 노드의 데이터를 출력하는 함수
def printNodes(start):
    current = start # 시작 위치부터 시작
    if current == None:  # 노드가 None일 때 함수에서 나옴
        return
    print(current.data, end=' ') # 첫 번째 노드 데이터 출력
    while current.link != None:  # 시작부터 노드의 끝까지 데이터 출력
        current = current.link
        print(current.data, end=' ')
    print()  # 줄 바꿈

# 새로운 노드를 리스트에 삽입하는 함수
def makeList(namePhone):
    global memory, head, current, pre # 전역변수를 사용

    # 새 노드 생성
    node = Node()
    node.data = namePhone
    memory.append(node)  # 메모리 리스트에 관리용으로 저장

    # 리스트가 비어있을 때, head가 방금 생성한 node를 바라보도록
    if head == None:
        head = node
        return

    # head가 새로운 노드보다 작을 때 head를 바꿔준다.
    if head.data[1] > namePhone[1]:
        # 이름이 아니라 height를 기준
        node.link = head
        head = node
        return

    # 중간 노드로 삽입하는 경우
    current = head
    while current.link != None:
        pre = current # 현재 노드를 pre로 저장
        current = current.link # 다음 노드로 이동
        if current.data[1] > namePhone[1]: # node를 삽입할 위치를 찾은 경우
            # current의 height가 더 크면 실행한다.
            pre.link = node # 이전 노드가 새로운 노드에 link 연결
            node.link = current # 새로운 노드가 현재 노드에 link를 연결해서 중간에 삽입
            return
    # 삽입하는 노드가 가장 큰 경우에 가장 끝에 연결
    current.link = node

# 전역 변수 선언
memory = []
head, pre, current = None, None, None
dataArr = [ ['지민', 180], ['정국',177], ['뷔',183],
           ['슈가',175], ['진',179] ]

# 메인 코드 부분
if __name__ == '__main__':
    for data in dataArr:
        makeList(data)
    printNodes(head)