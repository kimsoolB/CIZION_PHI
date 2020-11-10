#컴퓨터가 연산할 때 숫자인지 문자인지 알려주는 것이 타입. 정해진 규칙에 따라 인지합니다

num1 = 1 #숫자형
print(num1)

num2 = "1" #문자형
print(num2)

print(num1 + 10)
# print((num2 + 10)) srt not "int" err
print(type(num2))
print(type(num1))
print(num2 + "10") #110
print(20 + int(num2)) #21 숫자형으로 바꿔주네 오...