# 숫자 더하기_심화(4)
# - 매개변수로 여러 자료형으로 구성된 리스트를 받고, 그 값을 더해서 리턴하는 함수를 만들어보세요. 숫자 또는 숫자로 변환해서 더할 수 있는 것들만 더하고, 나머지는 무시하면 됩니다.

def recursiveSum(*user_list):
	result = 0
	
	for i in user_list:
		if isinstance(i, (int, float)):
			result += i
		elif isinstance(i, (list, tuple)):
			result += recursiveSum(*i)

	return result
	
print(recursiveSum(*[1, 2.4, 'abc', 'defg', (4, 5.7, (2, 3.1)), \
					 [6, 7], [3, [7, 2.01], [5, (3, 1.83), 7, 5.3, 4]]]))