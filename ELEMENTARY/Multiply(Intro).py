def mult_two(a, b):
    # your code here
    return a*b

# 인터프리터가 직접 실행했을 경우에만 if문 내의 코드 실행
# 모듈에서 import해서 실행하면 __name__ 변수에 '파일명'이 들어감
if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    # assert 결과 값이 틀리면 AssertionError 발생
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
