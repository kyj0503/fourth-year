## 함수 선언 ##
def findMinIndx(ary):
    minIdx = 0
    for i in range(1, len(ary)): #받은 array안에서 가장 작은 값의 index번호가 나온다.
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

## 전역 변수 ##
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

## 메인 코드 ##
if __name__ == "__main__":
    print("정렬 전 --> ", before)
    for _ in range(len(before)):
        minPos = findMinIndx(before) # minPos는 처음엔 4가 나온다.
        after.append(before[minPos]) # 정렬 후 배열에 하나씩 저장
        del(before[minPos])
    print("정렬 후 --> ", after)