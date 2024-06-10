# 랜덤함수 불러오기 (외장함수)
import random


# 업다운 게임 실행 함수
def up_down_game():
    # 컴퓨터가 1~100사이의 랜덤한 숫자를 생성
    answer = random.randint(1, 100)
    # 시도 횟수
    count = 10

    print("업다운 게임! 1에서 100사이의 숫자를 맞춰보세요!")
    while count > 0:
        # 사용자로부터   숫자 입력 받기
        user_input = int(input(f"숫자를 입력해주세요(남은 기회 : {count}) :"))
        # 사용자가 입력한 값이 정답일때

        # 정답일 경우 반복문을 빠져나감
        if user_input == answer:
            print("축하합니다. 정답입니다.")
            break

        # 시도 횟수 감소
        count -= 1
        if count == 0:
            print(f"게임 종료! 시도횟수를 다 사용하였습니다. 정답은 {answer}")
            break
        if user_input < answer:
            print("Up!")
        else:
            print("Down!")


up_down_game()