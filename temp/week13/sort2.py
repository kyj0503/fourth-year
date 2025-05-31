## 함수 선언 ##
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        print(f"{i}번째에서 기준이 되는 최소 시작값: {ary[i]}")
        for k in range(i+1, n):
            if(ary[minIdx] > ary[k]):
                minIdx = k
                print(f"{i}번째에서 찾은 최수값: {ary[k]}")
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

        print(f"{i}번째에서 값 변경 {ary[minIdx]} <-> {ary[i]}")
        print(ary, "\n")

    return ary

## 전역 변수 ##
dataAry = [188, 168, 177, 120, 88, 130, 77, 54, 230, 229]

if __name__ == "__main__":
    dataAry = selectionSort(dataAry)
    print('정렬 전--> ', dataAry)
    print('정렬 후--> ', dataAry)