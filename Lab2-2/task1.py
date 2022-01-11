import sys
numb = int(sys.argv[1])
count_of_dividers = 0

for i in range(numb, 1, -1):
    if (numb % i == 0):
        print(i, end = " ")
        count_of_dividers += 1
print("\nКількість дільників цього числа:", count_of_dividers)