def backward_string(val: str) -> str:
    # your code here

    # # 1. 전형적인 for문 활용(1)
    # result = ''
    # for i in reversed(val):
    #     result += i
    # return result

    # # 2. 전형적인 for문 활용(2)
    # for 변수 in reversed(range(횟수)):
    # for 변수 in reversed(range(시작, 끝)):
    # for 변수 in reversed(range(시작, 끝, 증가폭)):
    # (ex1) for i in reversed(range(10)) - 9부터 0까지 10번 반복

    # # (cf) 일반적인 for문
    # (ex1) for i in range(0, 10): - 1 ~ 10
    # (ex2) for i in range(10, 0, -1): - 10 ~ 1
    # (ex3) for i in val:

    # 3. 간단 명료 Ver.
    # (ex1) val[3:0:-1] - 3번 인덱스부터 1번 인덱스까지 역순으로 출력
    # (ex2) val[3::-1] - 3번 인덱스부터 0번 인덱스까지 역순으로 출력
    # (ex3) val[::-1] - 전체 문자열을 역순으로 출력(0번 인덱스부터 마지막 인덱스(생략가능)까지)
    return val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
