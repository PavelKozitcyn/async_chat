import locale

'''1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных'''

words_list = ["разработка","сокет","декоратор"]
bytes_1 = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
bytes_2 = b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
bytes_3 = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'

for el in words_list:
    print(type(el))
    print(el)

bytes_list = [bytes_1, bytes_2, bytes_3]

for el in bytes_list:
    print(type(el))
    print(el)


'''2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных''' 

bytes_4 = b'class'
bytes_5 = b'function'
bytes_6 = b'method'

bytes_list_1 = [bytes_4, bytes_5, bytes_6]

for el in bytes_list_1:
    print(type(el))
    print(el)
    print(len(el))


"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе."""

words_list1 = ['attribute', 'класс', 'функция','type']

for el in words_list1:
    try:
        print(bytes(el, 'ascii'))
    except UnicodeEncodeError:
        print(f'{el} невозможно записать в  байтовом типе')


"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode)."""

string_list = ['разработка', 'администрирование', 'protocol', 'standard']
list_to_utf8 = []
list_to_str =[]

for el in string_list:
    try:
        elm = el.encode("UTF-8", 'ignore')
        list_to_utf8.append(elm)
    except UnicodeEncodeError:
        print(f'{el} невозможно записать в  байтовом типе')

print(list_to_utf8)

for el in list_to_utf8:
    try:
        elm = el.decode('UTF-8','ignore')
        list_to_str.append(elm)
    except UnicodeEncodeError:
        print(f'{el} неправильная кодировка')

print(list_to_str)


"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице."""

import subprocess
import chardet

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

ARGS_2 = ['ping', 'youtube.com']
G_PING = subprocess.Popen(ARGS_2, stdout=subprocess.PIPE)
for line in G_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))


"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор». 
Проверить кодировку файла по умолчанию. 
Принудительно открыть файл в формате Unicode и вывести содержимое."""


def_coding = locale.getpreferredencoding()
print(def_coding)

F_N = open('test_file.txt', 'w')
F_N.write('сетевое программирование сокет декоратор')
F_N.close()
print(type(F_N))

with open('test_file.txt','r', encoding='utf-8') as lr1:
    for line in lr1:
        print(line, end="")
