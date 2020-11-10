#함수 안에서 변수 사용하기
#중간결과 저장, 출력하고 사칙연산에 적용해보기

def plus(val1, val2):
    print(val1 + val2)

plus(20, 30)

def plus(val1, val2):
    result = val1 + val2
    print(val1 + val2)

plus(20, 30) #same result

def plus2(val1, val2):
    print(val1 + val2 * 2)

plus2(20, 30)

def plus2(val1, val2):
    mid = val2 * 2
    print("mid:", mid)
    result = val1 + mid
    print(result)

plus2(20, 30)