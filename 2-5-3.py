"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, 
которые повторяются в нём более одного раза. Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

Sample Input 1:
4 8 0 3 4 2 0 3
Sample Output 1:
0 3 4

Sample Input 2:
10
Sample Output 2:

Sample Input 3:
1 1 2 2 3 3
Sample Output 3:
1 2 3

Sample Input 4:
1 1 1 1 1 2 2 2
Sample Output 4:
1 2
"""
s = list(int(i) for i in input().split())
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
res = []
for i in d.keys():
    if d[i] >= 2:
        res.append(i)
print(*res)
