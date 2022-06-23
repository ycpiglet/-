# 숫자 맞히기 게임_심화(2)
#- 숫자 맞히기가 아니라 단어(문자열) 맞히기로 예제를 수정해보세요. 사전 순서로 정렬된 단어 리스트를 미리 만들고, 이를 사용자에게 보여주세요. 그리고 이 중에서 하나를 맞히라고 물어보기 바랍니다. 사용자가 어떤 단어를 예측하면 답이 사전 순서에서 더 앞에 있는지 또는 뒤에 있는지 알려주기 바랍니다.

import random

def guessing_game():
	list = ['elephant', 'banana', 'gold', 'candy', 'apple', 'fire', 'daisy']
	list.sort()
	answer = list[random.randint(0, len(list))]

	print(list)
	print("Guess any word in the list")
	
	while True:
		user_data = input()

		if user_data in list:
			index1 = list.index(answer)
			index2 = list.index(user_data)
	
			if index1 < index2:
				print("It's behind the answer. Try again.")
			elif index1 == index2:
				print(f"Congraturation! The answer is {answer}")
				break
			else:
				print("It's in front of the answer. Try again.")

		else:
			print("Please type correctly.")

guessing_game()