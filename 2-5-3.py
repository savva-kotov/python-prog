"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
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
s.sort()
n = 0
l = len(s) - 1
t = []
if len(s) == 1:
    print()
else:
    for i in range(l):
        if s[i] == s[i + 1]:
            n += 1
            continue
        elif i == 0 and s[i] != s[i + 1]:
            continue
        elif len(s) == 1:
            break
        elif i != 0 and s[i] != s[i - 1] and s[i] != s[i + 1]:
            continue
        else:
            t.append(s[i])
            n = 1
    if s[l] == s[l - 1]:
        t.append(s[l])
    t.sort()
    for i in range(len(t)):
        print(t[i], end=" ")
