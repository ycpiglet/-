# 숫자 맞히기 게임
# - guessing_game()이라는 매개변수 없는 함수를 만듭니다.
# - 이 함수를 실행하면 0~100 사이의 숫자 중에서 랜덤한 숫자 하나를 뽑습니다.
# - 이어서 사용자에게 숫자를 맞춰보라며, 숫자 입력을 요구합니다.
# - 사용자가 숫자를 입력할 때마다, 프로그램은 숫자에 따라서 다음과 같은 결과를 출력합니다.
# · Too high(큽니다)
# · Too low(작습니다)
# · Just right(정답입니다)
# - 숫자를 맞췄다면 프로그램을 종료합니다. 이외의 경우에는 다시 입력을 요구합니다.
# - 프로그램은 사용자가 숫자를 맞혔을 경우에만 종료합니다.

import random

def guessing_game():
	answer = random.randint(0, 100)

	print("Guess any number between 0 and 100")
	
	while True:
		user_data = int(input())
		
		if user_data > answer:
			print("It's too high! Try again")
		elif user_data == answer:
			print(f"Congraturation! The answer is {answer}")
			break
		else:
			print("It's too low! Try again")

guessing_game()