## 함수 선언 ##
def findsertIdx(ary, data): # data를 삽입할 위치를 찾는 알고리즘(삽입정렬)
    findIdx = -1 # 초기값
    for i in range(0, len(ary)):
        if (ary[i] > data): # ary[i]을 data와 비교하면서 안에 값이 더 크면 findIdx를 i번으로 바꾼다.
            findIdx = i
            break
    if findIdx == -1: # 더 큰 값을 못 찾으면 제일 마지막 위치로
        return len(ary)
    else: # 아니면 입력할 위치 return
        return findIdx

## 전역 변수 ##
before = [188, 162, 168, 129, 50, 150, 177, 105, 199]
after = []

## 메인 코드
if __name__ == '__main__':
    print('정렬 전-->', before)
    for i in range(len(before)):
        data = before[i]
        insPos = findsertIdx(after, data)
        after.insert(insPos, data) #입력할 위치에 data insert하기
    print('정렬 후-->', after)
