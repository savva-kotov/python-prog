"""
Программа должна считывать размеры команд (два положительных целых числа a и b, каждое число вводится на отдельной строке) и выводить наименьшее число d
, которое делится на оба этих числа без остатка.

Sample Input 1:
7
5
Sample Output 1:
35

Sample Input 2:
15
15
Sample Output 2:
15

Sample Input 3:
12
16
Sample Output 3:
48
"""

a = int(input())
b = int(input())
ra = a
rb = b
while ra != rb:
    if ra < rb:
        ra += a
    else: 
        rb += b

print(rb)
