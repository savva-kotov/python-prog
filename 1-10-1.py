'''
Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A A A часов в сутки, но пересыпать тоже вредно 
и не стоит спать более B B B часов. Сейчас Аня спит H H H часов в сутки. Если режим сна Ани удовлетворяет рекомендациям 
передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее A A A часов, выведите “Недосып”, если же более B B B часов, 
то выведите “Пересып”. Получаемое число A A A всегда меньше либо равно B B B.
На вход программе в три строки подаются переменные в следующем порядке: A A A, B B B, H H H.
Обратите внимание на регистр символов: вывод должен в точности соответствовать описанному в задании, 
т. е. если программа должна вывести "Пересып", выводы программы "пересып", "ПЕРЕСЫП", "ПеРеСыП" и другие не будут считаться 
верными. Это первое не самое тривиальное задание на условное выражение. 
В случаях, когда разбить исполнение программы на несколько направлений, стоит внимательно обдумать все условия, 
которые нужно использовать. Особое внимание стоит уделить строгости используемых условных операторов: 
различайте < \lt < и ≤ \le ≤; > \gt > и ≥ \ge ≥. Для того, чтобы понимать, какой из них стоит использовать, 
внимательно прочитайте условие задания.

Sample Input 1:
6
10
8
Sample Output 1:
Это нормально

Sample Input 2:
7
9
10
Sample Output 2:
Пересып

Sample Input 3:
7
9
2
Sample Output 3:
Недосып
'''
A = int(input())
B = int(input())
H = int(input())

# A -- H -- B
if (H < A):
    print('Недосып')
elif (H > B):
    print('Пересып')
else:
    print('Это нормально')

