def is_all_upper(text: str) -> bool:
    # your code here

    # text.capitalize() : 첫글자만 대문자로 변환
    # text.upper() : 전체 문장 대문자로 변환
    # text.lower() : 전체 문장 소문자로 변환

    # text.isupper() : 전체 문장이 대문자인지 판단
    # text.islower() : 전체 문장이 소문자인지 판단
    # text.isspace() : 전체 문장이 공백인지 판단

    # return text.isupper() : 공백의 경우는 false 출력

    # 공백의 경우에도 true 출력 가능
    return text.upper()==text

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
