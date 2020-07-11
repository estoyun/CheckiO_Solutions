def end_zeros(num: int) -> int:
    # your code here
    # str.rstrip([chars]) : 문자열의 끝 삭제(기본값은 공백)
    # num의 자릿수 - 맨 뒤의 0을 삭제한 후 남은 문자의 개수
    return len(str(num)) - len(str(num).rstrip('0'))


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
