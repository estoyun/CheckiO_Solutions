from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here

    # 슬라이싱으로 문자열 나누기 (one-liner)
    # (ex) a[1:] a[1]이 포함됨(a[1]부터) / a[:1] a[1]이 포함되지 않음(a[0]까지)
    return items[1:] + items[:1]


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
