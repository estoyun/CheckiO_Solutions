from typing import Iterable

# Iterable 객체 - 반복 가능한 객체 (for문의 in 키워드 뒤에 올 수 있는 모든 값)
# 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range
def remove_all_before(items: list, border: int) -> Iterable:
    # your code here

    """
    1. 일반적인 풀이법
     for i in items:
         if i == border:
             return items[items.index(i):]
     return items
    """

    # 2. 고수들의 풀이법 (고수특 : 한 줄로 끝냄(one-liner))
    return items[items.index(border):] if border in items else items

    '''
    (ex) traditional if-else

     if x > 0:
         value = 10
     else:
         value = 20

    (ex) one-liner

    value = 10 if x > 0 else 20
    '''

    '''
    (ex2) traditional if-elif-else

    alpha = 10

    if alpha > 7:
        beta = 999
    elif alpha == 7:
        beta = 99
    else:
        beta = 0

    (ex2) one-liner

    beta = 999 if alpha > 7 else (beta == 99 if alpha == 7 else 0)
    '''

if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
