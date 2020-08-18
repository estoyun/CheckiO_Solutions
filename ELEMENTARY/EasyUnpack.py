# "리스트"는 [ ]으로 둘러싸지만, "튜플"은 ( )으로 둘러싼다.
# "리스트"는 그 값의 생성, 삭제, 수정이 가능하지만 "튜플"은 그 값을 바꿀 수 없다.
# "튜플"은 변경이 불가능하기 때문에 처리 속도가 빠르다.
def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here
    return (elements[0], elements[2], elements[-2])

if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
