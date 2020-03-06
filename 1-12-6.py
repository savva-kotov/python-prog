"""
Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное), выводящее это число в консоль 
вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми, 
например: 1 программист, 2 программиста, 5 программистов.
В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, 
как минимум до 1000 человек.
Дополнительный комментарий к условию:
Обратите внимание, что задача не так проста, как кажется на первый взгляд. Если ваше решение не проходит какой-то тест, 
это значит, что вы не рассмотрели какой-то из случаев входных данных (число программистов 0≤n≤1000). 
Обязательно проверяйте свои решения на дополнительных значениях, а не только на тех, что приведены в условии задания.
Так как задание повышенной сложности, вручную код решений проверяться не будет. 
Если вы столкнулись с ошибкой в первых четырёх тестах, проверьте, что вы используете только русские символы для ответа. 
В остальных случаях ищите ошибку в логике работы программы.

Sample Input 1:
5
Sample Output 1:
5 программистов

Sample Input 2:
0
Sample Output 2:
0 программистов

Sample Input 3:
1
Sample Output 3:
1 программист

Sample Input 4:
2
Sample Output 4:
2 программиста
"""
# put your python code here
s = int (input())
n1 =" программистов"
n2 =" программист"
n3 =" программиста"
if  s>=0:
  if s==0:
    print(str(s) + n1)
  elif s%100>=10 and s%100<=20:
    print(str(s) + n1)
  elif s%10==1:
    print(str(s) + n2)
  elif s%10>=2 and s%10<=4:
    print(str(s) + n3)
  else:
    print(str(s) + n1)


