import sys

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    print("========== 현재 노드 정보 ==========")
    if start is None:
        print("(리스트가 비어 있습니다)")
    else:
        current = start
        print(current.data, end=" ")

        while current.link != start:
            current = current.link
            print(current.data, end=" ")
        print() # 줄바꿈
    print("===============================")

def insertNode(findData, insertData):
    global memory, head, current, pre

    node = Node()
    node.data = insertData
    memory.append(node)

    if head == None:
        head = node
        node.link = head
        return True

    if head.data == findData:
        # 마지막 노드를 찾아 링크 수정
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        node.link = head
        head = node # head를 새 노드로 변경
        return True

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            pre.link = node
            node.link = current
            return True

    return False

def deleteNode(deleteData):
    global memory, head, current, pre

    if head == None:
        return False

    # Case 1: 삭제할 노드가 head일 때
    if head.data == deleteData:
        current_to_delete = head
        # 리스트에 노드가 하나뿐일 때
        if head.link == head:
            memory.remove(head)
            head = None
        # 노드가 여러 개일 때
        else:
            # 마지막 노드를 찾아 head의 다음 노드를 가리키게 함
            last = head
            while last.link != head:
                last = last.link
            head = head.link # head 변경
            last.link = head # 마지막 노드가 새 head를 가리키도록
            memory.remove(current_to_delete)
        del(current_to_delete)
        return True

    # Case 2: 중간 또는 마지막 노드 삭제
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            memory.remove(current)
            del(current)
            return True

    return False

def findNode(findData):
    global memory, head, current, pre

    if head == None:
        return None

    current = head
    if current.data == findData:
        return current
    while current.link != head:
        current = current.link
        if current.data == findData:
            return current

    return None

memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    if dataArray:
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
            node.link = head # 마지막 노드가 head를 가리키도록
            memory.append(node)

    while True:
        printNodes(head)

        print("============= 메뉴 =============")
        print("1: 삽입, 2: 삭제, 3: 검색, 4: 종료")
        print("===============================")

        select = input("메뉴를 선택해 주세요:")

        if select == '1': # 삽입
            find_data = input("삽입할 노드의 위치를 입력해 주세요:")
            insert_data = input("삽입할 데이터를 입력해 주세요:")
            if not insertNode(find_data, insert_data):
                 print(f"  -> 삽입 실패: 데이터 '{find_data}'를 찾을 수 없습니다.")
                 pass

        elif select == '2': # 삭제
            delete_data = input("삭제할 데이터를 입력해 주세요:")
            if not deleteNode(delete_data):
                print("삭제할 노드가 없습니다.")

        elif select == '3': # 검색
            find_data = input("검색할 데이터를 입력해주세요:")
            found_node = findNode(find_data)
            if found_node:
                print(f"{found_node.data} 이 검색 되었습니다.")
            else:
                print("검색할 데이터가 없습니다.")

        elif select == '4': # 종료
            print("프로그램을 종료합니다.")
            sys.exit()

        else:
            print("잘못된 메뉴 선택입니다. 다시 입력해주세요.")

        print()