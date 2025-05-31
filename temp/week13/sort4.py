def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if ary[cur-1] > ary[cur]:
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1] #서로의 값을 바꾸기 (tmp없이 가능)
    return ary

## 전역 변수 ##
dataAry = [188, 168, 177, 120, 88, 130, 77, 54, 230, 229]

## 메인 코드 ##
if __name__ == '__main__':
    print('정렬 전-->', dataAry)
    dataAry = insertionSort(dataAry)
    print('정렬 후-->', dataAry)