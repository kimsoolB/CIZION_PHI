def printGugudan():
    for num in range(1, 10):
        print(2, "*", num, "=", 2 * num) #알아서 한 칸씩 띄어짐. 붙일 수 없음. 포맷은 조절가능

printGugudan()

def print3dan():
    for num in range(1, 10):
        st = "{} * {} = {}".format(3, num, 3 * num)
        print(st)

print3dan()