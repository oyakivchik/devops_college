import sys
num = int(sys.argv[1])
co = 0

for i in range(num):
	i = i + 1
	if(num % i == 0):
		print('Дільник для числа ', num,' є ', i)
		co = co + 1

print('К-сть дільників для числа ', num,' = ', co)