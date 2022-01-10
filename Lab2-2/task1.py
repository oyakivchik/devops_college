import sys
num = int(sys.argv[1])
amount = 0

for i in range(num):
	i = i + 1
	if(num % i == 0):
		print('Divider for number -', num,' is ', i)
		amount = amount + 1

print('Amount divider for number -', num,' = ', amount)