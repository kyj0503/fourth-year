
# 왼쪽 열 코드
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end = " ")
    while current.link != start:
        current = current.link
        print(current.data, end = " ")
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

# 오른쪽 열 코드
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node
    node.link = head

def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def findNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != head:
        current = current.link
        if current.data == findData:
            return current
    return Node() # 빈 노드 반환

memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

# 오른쪽 열 코드
if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)
    printNodes(head)

    #노드 삽입 테스트 코드
    insertNode("다현", "화사") # 첫번째 노드 삽입
    printNodes(head)
    insertNode("사나", "솔라") # 중간 노드 삽입
    printNodes(head)
    insertNode("재남", "문별") # 마지막 노드 삽입
    printNodes(head)

    # 노드 삭제 테스트 코드
    deleteNode("다현")  # 첫번째 노드 삭제
    printNodes(head)

    deleteNode("쯔위")  # 첫번째 외 노드 삭제
    printNodes(head)

    deleteNode("지효")  # 마지막 노드 삭제
    printNodes(head)

    deleteNode("재남")  # 없는 노드 삭제
    printNodes(head)

    # 노드 검색 테스트 코드
    printNodes(head)
    fNode = findNode("화사")  # 첫번째 노드 검색
    print(fNode.data)

    fNode = findNode("정연")  # 중간 노드 검색
    print(fNode.data)

    fNode = findNode("재남")  # 없는 노드 검색
    print(fNode.data)