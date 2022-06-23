# 숫자 더하기_심화(3)
# - 단어(문자열)로 구성된 리스트를 매개변수로 받고, (가장_짧은_단어_길이, 가장_긴_단어_길이, 단어_길이의 _평균) 형태의 튜플을 리턴하는 함수를 만들어보세요.

def word_len(list):
	length = []
	long = ''
	short = ''
	result = 0
	
	for i in list:
		length.append(len(i))
		result += len(i)

	long = list[length.index(max(length))]
	short = list[length.index(min(length))]
	mean = result/len(list)
	return (short, long, mean)

print(word_len(['apple', 'banana', 'sea', 'dish', 'elephant', 'go']))