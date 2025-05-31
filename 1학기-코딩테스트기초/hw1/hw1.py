# 전역 리스트를 사용해 곱셈 과정을 저장 (n, n-1, ..., m)
steps = []

def factorial_down(cur, stop):
    """
    재귀함수
    cur부터 stop까지(내림차순) 곱을 구한다.

    예: cur=5, stop=3 -> 5 x 4 x 3
    steps 리스트에 문자열을 저장하여 곱셈 과정을 기록한다.

    종료 조건:
    if cur < stop: return 1
    (더 이상 곱할 값이 없으면 1을 반환)
    """
    if cur < stop:
        return 1
    steps.append(str(cur))
    return cur * factorial_down(cur - 1, stop)

def main():
    while True:
        # 1) n 입력
        n = int(input("몇 팩토리얼? (0 입력시 종료): "))
        if n == 0:
            print("안녕 잘가")
            break

        # 2) m 입력
        m = int(input("어디서 멈출래?: "))

        # m이 0 이하면 오류 메시지 후 다시 입력
        if m <= 0:
            print("멈추는 값이 너무 작잖아! 다시 입력해!")
            continue

        # m이 n보다 크면 오류 메시지 후 다시 입력
        if m > n:
            print("멈추는 값이 너무 크잖아! 다시 입력해!")
            continue

        # 정상 범위이면, 재귀 함수를 통해 부분 팩토리얼 계산
        # 매번 steps 리스트를 비우고 다시 사용
        global steps
        steps = []  # 곱셈 과정 저장용 리스트 초기화

        result = factorial_down(n, m)  # n부터 m까지 곱 (n >= m)

        # 곱셈 과정 문자열로 만들기: steps = ["n", "n-1", ..., "m"]
        expression = " x ".join(steps)

        print(f"{n} ! : {expression} = {result}")

# 메인 함수 실행
if __name__ == "__main__":
    main()
