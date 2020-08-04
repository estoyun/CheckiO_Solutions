def beginning_zeros(number: str) -> int:
    # your code here
    
    # strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
    # rstrip([chars]) : 인자로 전달된 문자를 String의 왼쪽에서 제거합니다.
    # lstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.
    return len(str(number)) - len(str(number).lstrip('0'))


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
