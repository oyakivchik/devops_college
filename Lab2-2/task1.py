import sys
num = int(sys.argv[1])
count = 0

for i in range(num):
	i = i + 1
	if(num % i == 0):
		print('Дільник для числа ', num,' є ', i)
		count = count + 1

print('Кількість дільників для числа ', num,' = ', count)