def print2dan():
    for num in range(1, 9 + 1):
        st = "{} * {} = {}".format(2, num, 2 * num)
        print(st)

def print3dan():
    for num in range(1, 9 + 1):
        st = "{} * {} = {}".format(3, num, 3 * num)
        print(st)

print2dan()
print3dan()