'''
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d d d 
и два числа: key key key и value value value.
Если ключ key key key есть в словаре d d d, то добавьте значение value value value в список, который хранится по этому ключу.
Если ключа key key key нет в словаре, то нужно добавить значение в список по ключу 2∗key 2 * key 2∗key. 
Если и ключа 2∗key 2 * key 2∗key нет, то нужно добавить ключ 2∗key 2 * key 2∗key в словарь и сопоставить ему список из переданного элемента [value] [value] [value].
Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''
# не добавляйте кода вне функции
def update_dictionary(d, key, value):
  if key in d:
    d[key]+=[value]
  if key not in d:
    if key*2 in d:
      d[key*2]+=[value]
    if key*2 not in d:
      d[key*2]=[value]

# не добавляйте кода вне функции

