def mysum(*numbers):
	print("Type some numbers")
	numbers = input().split(',')
	result = 0
	
	for number in numbers:
		result += int(number)

	return(result)

print(mysum())