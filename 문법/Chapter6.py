# Chapter6. 반복문
# 반복문
# 반복해서 코드를 사용해야될때 for, while
# for : 반복횟수가 정해져있거나, 리스트와같은 시퀀스데이터의 각 항목을 반복할때
for i in range(5):
    print(i)

my_list = ["apple", "hamburger", "pizza", "mango"]

for food in my_list:
    print(food)
    if food == "pizza":
        print("피자가 좋아요")

# range : 연속되는 범위를 지정해주는 시퀀스데이터
# range(end) 0부터 end -1 까지의 범위
# range(start,end) start 부터 end -1 까지의 범위
# range(start,end,step) start 부터 end -1 까지 step 만큼 건너뛴 범위

# i=3 i<10 i++
for i in range(3, 10):
    print(i)

# i=10 i<100 i+=10
for i in range(10, 100, 10):
    print(i)

# while : 조건에 따라 반복문의 흐름을 제어하거나, 무한루프


money = 5000

while money > 0:
    money -= 1000
    # money = money-1000
    print("1000원을 사용했습니다. 현재 돈 :", money)

print("남은돈 ", money)

# while True:
#   print("무한루프")


# break : 반복문을 도중에 빠져나오고싶을때
for i in range(10):
    print(i)
    if i >= 8:
        break

my_list = ["apple", "hamburger", "pizza", "mango"]

for food in my_list:
    print(food)
    if food == "pizza":
        print("피자가 좋아요")
        break

i = 0
while True:
    i += 1
    print(i)
    if i > 50:
        print("50보다 커서 종료됩니다.")
        break
