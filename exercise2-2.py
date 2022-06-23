# 숫자 더하기_심화(2)
# - 매개변수로 숫자 리스트를 받고, 숫자의 평균을 계산하는 함수를 만들어보세요.

def mysum(*list):
	result = 0
	
	for number in list:
		result += number

	mean = result/len(list)
	return(mean)

print(mysum(*[1, 2, 3, 4, 5, 6]))