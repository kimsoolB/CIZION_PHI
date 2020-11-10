import datetime

now = datetime.datetime.now()

file = open("./log.txt", "w+")
for i in range(30):
    now += datetime.timedelta(seconds=10)
    file.write("{}".format(now))
file.close()