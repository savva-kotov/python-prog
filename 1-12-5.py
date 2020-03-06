"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки 
сначала максимальное, потом минимальное, после чего оставшееся число. На ввод могут подаваться и повторяющиеся числа.

Sample Input 1:
8
2
14
Sample Output 1:
14
2
8

Sample Input 2:
23
23
21
Sample Output 2:
23
21
23
"""

a = int(input())
b = int(input())
c = int(input())
print(list(reversed(sorted([a,b,c])))[0]) #сортируем, разворачиваем и берем первый элемент;
print(list(reversed(sorted([a,b,c])))[2])
print(list(reversed(sorted([a,b,c])))[1])

или

print('\n'.join(str(value) for value in sorted([int(input()) for i in range(3)])))
