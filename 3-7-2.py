"""
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. 
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, 
на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, 
и ещё одна строка, которую нужно расшифровать.
Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%
Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. 
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:
*d*%*d*#*d*
dacabac

Sample Input 2:
dcba
badc
dcba
badc
Sample Output 2:
badc
dcba
"""

a = [i for i in input()]#символы
a1 = [i for i in input()]#код символов
b = input()#строка для шифровки
b1 = input()#строка для дешифровки

bb = ''
for i in b:
  bb += a1[a.index(i)]

b11 =''
for i in b1:
  b11+= a[a1.index(i)]

print(bb)
print(b11)

