def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    # 1. 일반적인 답
    if text[len(text)-1] != "." :
        return text[0].upper()+text[1:]+"."
    return text[0].upper()+text[1:]

    # # 2. one-liner
    # lstrip(왼)/rstrip(오)/strip(왼,오) - 인자가 있으면 해당 문자와 동일한 것 모두 제거
    # return text[0].upper() + text[1:].rstrip('.') + '.'


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
