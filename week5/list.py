#전역변수 선언
katok = []
select = -1

#선형 리스트 데이터 추가
def Add_data(friend):
    katok.append(None)
    katok[len(katok)-1] = friend

#선형 리스트 데이터 삽입
def Insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("범위를 벗어났습니다.")
        return

    katok.append(None)

    for i in range(len(katok)-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

#선형 리스트 데이터 삭제
def Delete_data(position):
    if position < 0 or position > len(katok):
        print("범위를 벗어났습니다.")
        return

    katok[position] = None

    for i in range(position+1, len(katok)):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[len(katok)-1])

#메인 코드 부분
if __name__ == "__main__":
    while(select != 4):
        select = int(input("(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)-->"))
        if (select == 1):
            data = input("입력할 데이터-->")
            Add_data(data)
            print(katok)
        if (select == 2):
            pos = int(input("입력할 위치-->"))
            data = input("입력할 데이터-->")
            Insert_data(pos, data)
            print(katok)
        if (select == 3):
            pos = int(input("입력할 위치-->"))
            Delete_data(pos)
            print(katok)
        if (select == 4):
            print("종료")
            exit
        else:
            print("1~4 중 하나를 입력하시오")
            continue