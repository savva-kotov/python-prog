"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое последнего файла из набора, как ответ на это задание.
"""

import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
a = [i for i in r.text.splitlines()]
u = 'https://stepic.org/media/attachments/course67/3.6.3/'
c = 0
while 'We' not in r.text:
    rr = requests.get(u+r.text)
    c+=1
    print(c)
print(c)
print(r.text)