def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    # string.join(iterable) -> iterable : member를 하나씩 변환할 수 있는 object(list, str, tuple)
    # replace(old, new, [count]) -> count는 왼쪽부터 바꿀 횟수, 생략가능
    return (",".join(phrases)).replace("right","left")

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
