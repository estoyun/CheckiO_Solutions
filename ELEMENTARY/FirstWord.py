def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    # split() 함수처럼 괄호 안에 아무 값도 넣지 않으면 공백(스페이스, 탭, 엔터)를 기준으로 문자열 나눔
    return text.split()[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
