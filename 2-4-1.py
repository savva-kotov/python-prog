'''
GC-состав является важной характеристикой геномных последовательностей и определяется как процентное соотношение суммы всех 
гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности. Напишите программу, которая вычисляет 
процентное содержание символов G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых 
символов).

Sample Input:
acggtgttat

Sample Output:
40.0
'''
st = input()
cnt = 0

for G in st:
    if (G == 'G') or (G == 'g'):
        cnt += 1

for C in st:
    if (C == 'C') or (C == 'c'):
        cnt += 1    

print((cnt/len(st))*100)

