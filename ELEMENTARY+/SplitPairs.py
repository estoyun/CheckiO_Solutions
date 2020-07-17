def split_pairs(a):
    # your code here

    # # 1. 일반 답
    # # 문자열의 길이가 홀수인 경우만 '_' 추가
    # a += '_'*(len(a)%2)
    # return [a[i:i+2] for i in range(0,len(a),2)]

    # # 2. recursive
    # # a[100:]처럼 list index 넘어가면 []가 됨

    # l = len(a)
    # if l == 0:
    #     return []
    # if l == 1:
    #     return [a + '_']
    # else:
    #     return [a[:2]] + split_pairs(a[2:])

    # 3. 경이로운 one-liner solution
    return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]

    # arr[::2] : 처음부터 끝까지 두 칸 간격으로 - (ex) [0,2,4,6,8]
    # arr[1::2] : index 1부터 끝까지 두 칸 간격으로 - (ex) [1,3,5,7,9]

    # zip() : 같은 길이의 리스트를 같은 인덱스끼리 잘라서 리스트로 반환을 해주는 역할

    # # (ex) Result ('a',1), ('b',2) - zip()
    # name = ['a', 'b']
    # value = [1, 2]
    
    # for n, v in zip(name, value):
    #     print(n, v)

    # # (cf) Result : ('a','b'), (1,2) - 일반
    # name = ['a', 'b']
    # value = [1, 2]
    
    # for n, v in name, value:
    #     print(n, v)

    # # for문 one-liner

    # (ex) v = list(range(10))
    # [0,1,2,3,4,5,6,7,8,9]

    # for i in v:
    # print(i)
    
    # [i for i in v]
    
if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
