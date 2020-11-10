def printNdan(dan):
    for num in range(1, 10):
        st = "{} * {} = {}".format(dan, num, dan * num)
        print(st)
    print("---------------------")

# printNdan(2)
# printNdan(3)
# printNdan(4)

for dan in range(2, 10):
    printNdan(dan)

printNdan(dan)