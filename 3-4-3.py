"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана
следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку 
по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку 
по всем абитуриентам:
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
"""

f = open('dataset_3363_4.txt','r')
a = {}#словарь с ученика и их баллами
b = []#баллы учеников
s = ''
res = [0,0,0]#среднее значение баллов учеников по 3 предметам

for i in f:
    s = i.replace('\n','').split(';')
    if s[0] not in a:
        a[s[0]] = (int(s[1]) + int(s[2]) + int(s[3]))/3
    else:
        a[s[0]] = (int(s[1]) + int(s[2]) + int(s[3]))/3      
    b.append(s[1:4])
    

f.close()
for i in b:
    res[0]+=int(i[0])
    res[1]+=int(i[1])
    res[2]+=int(i[2])  

res = list(map(lambda x: x / len(b), res))

for i in a.values():
    print(i)
print(res)
