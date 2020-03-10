"""
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке 
число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.

Sample Input 1:
a aa abC aa ac abc bcd a
Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2

Sample Input 2:
a A a
Sample Output 2:
a 3
"""

import collections
c = collections.Counter()

l = input().lower().split()
for word in l:
    c[word] +=1
for key,value in c.items():
    print(key,value)
