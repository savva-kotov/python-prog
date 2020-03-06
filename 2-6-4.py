"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end
Sample Output 2:
4
"""

import copy
a = []
b = [i for i in input().split()]
while b != ['end']:
  a.append(b)
  b = [i for i in input().split()]

for i in range(len(a)):
  a[i]=list(map(int,a[i]))

c = copy.deepcopy(a)
for i in range(len(a)):
  for j in range(len(a[i])):
    c[i][j] = a[i][j-len(a[i])+1] + a[i][j-1] + a[i-len(a)+1][j] + a[i-1][j]

s = ''
for ii in range(len(c)):
    for i in c[ii]:    
        s+=str(i)
        s+=' '
    print(s)
    s=''

