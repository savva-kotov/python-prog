"""
Напишите программу, которая принимает на стандартный вход список игр футбольных 
команд с результатом матча и выводит на стандартный вывод сводную таблицу 
результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n
— количество завершенных игр.
После этого идет n
строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
    
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.

Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2

Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
"""

inp=int(input())
res = {}#словарь со списком всех команд (Команда:Всего_игр Побед Ничьих Поражений Всего_очков)

for i in range(inp):
    a = [i for i in input().split(';')]#превращаем входную строку в список
    if a[0] not in res:
        res[a[0]] = [1,0,0,0,0]#если нет в списке, то до добавляем
    else:
        res[a[0]][0] += 1#если есть, то увеличиваем счетчик игр
    
    if a[2] not in res:
        res[a[2]] = [1,0,0,0,0]
    else:
        res[a[2]][0] += 1
        
    if a[1] > a[3]:#если победила команда 1 (команда 2 проиграла)
        res[a[0]][1] += 1#увеличиваем счетчик побед команды 1
        res[a[0]][4] += 3#увеличиваем очки команды 1
        res[a[2]][3] += 1#увеличиваем счетчик поражений команды 2
        
    elif a[1] < a[3]:#если победила команда 2 (команда 1 проиграла)
        res[a[0]][3] += 1
        res[a[2]][1] += 1
        res[a[2]][4] += 3
        
    else:#ничья
        res[a[0]][2] += 1#увеличиваем счетчик ничей
        res[a[2]][2] += 1
        res[a[0]][4] += 1#увеличиваем очки
        res[a[2]][4] += 1



for i in res.items():
    print(i[0] + ':' + ' '.join(map(str, i[1])))
