# import numpy as np

def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
        0을 포함한 짝수 인덱스의 값들의 합과 리스트 맨 마지막 값의 곱 연산 결과 출력
    """
    return 0 if array==[] else sum(array[i] for i in range(0,len(array),2))*array[len(array)-1]

    # # one-liner(speedy)
    # return sum(array([::2])*array[-1] if array!=[] else 0

    # # 3rd party solution
    # aux = np.array(array)
    # if(aux.size<1): return 0
    # else: return aux[aux.size-1]*aux[0::2].sum(0)
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
