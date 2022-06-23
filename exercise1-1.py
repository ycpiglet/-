# 숫자 맞히기 게임_심화(1)
# - 이번 프로그램을 수정해서, 사용자가 숫자를 예측해볼 기회를 3번까지로 제한해보세요. 만약 사용자가 3번의 기회 동안 답을 맞히지 못했다면 사용자가 맞히지 못했다고 알려주고 프로그램을 종료해주세요.

import random

def guessing_game():
	answer = random.randint(0, 100)
	chance = 3
	
	print("Guess any number between 0 and 100. You have 3 chances.")
	
	while True:
		user_data = int(input())
		
		if user_data > answer:
			print("It's too high! Try again")
		elif user_data == answer:
			print(f"Congraturation! The answer is {answer}")
			break
		else:
			print("It's too low! Try again")

		chance -= 1	

		if chance == 0:
			print("Sorry. There are no more chances.")
			break

guessing_game()