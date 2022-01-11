import sys

numb = int(input("Введить ціле число: "))
count = 2;
print("Дільники:", numb, end = " ")
for i in range(numb - 1, 1, -1):
    if (numb % i == 0):
        print(i, end = " ")
        count += 1
print (1)
print("К-сть дільників:", count)
