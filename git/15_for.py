#컴퓨터는 반복에 특화되어있다
#range(start, stop, step)
#함수 안에 두줄, 포문 안에 한 줄
def print2to20():
    for num in range(2, 20 + 1, 2):
        print(num)

print2to20()

def print2to22():
    for num in range(1, 10 + 1):
        print(num * 2)
print2to22()