# Задание 1 1. Каждое из слов «разработка», «сокет», «декоратор»
# представить в строковом формате и проверить тип и содержание соответствующих
# переменных. Затем с помощью онлайн-конвертера преобразовать строковые
# представление в формат Unicode и также проверить тип и содержимое переменных.

r = 'Разработка'
s = 'Сокет'
d = "Декоратор"

def type_checker(a,b,c):
    print(type(a),a)
    print(type(b),b)
    print(type(c),c)

type_checker(r,s,d)

def bt_checker(a,b,c):
    a = a.encode('utf-8')
    b = b.encode('utf-8')
    c = c.encode('utf-8')
    a = a.decode('utf-8')
    b = b.decode('utf-8')
    c = c.decode('utf-8')
    type_checker(a,b,c)

bt_checker(r,s,d)
print(2)
# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

c = bytes('class', 'utf-8')
f = bytes('function', 'utf-8')
m = bytes('method', 'utf-8')
print(type(c),c, len(c))
print(type(f),f, len(f))
print(type(m),m, len(m))

print(3)
#  Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
try:   # Но здесь не выбрасывается исключение, зачем try/exept?
    a = bytes('attribute', 'utf-8')
    c = bytes('класс', 'utf-8')
    f = bytes('функция', 'utf-8')
    t = bytes('type', 'utf-8')
    print(a, c, f, t)
    print(t, 'Невозможно записать в байтовом типе')
except:
    print('Exeption')

print(4)
# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

r = 'разработка'
a = 'администрирование'
p = 'protocol'
s = 'standard'

for i in (r,a,p,s):
    i = i.encode('utf-8')
    print(i)
    i = i.decode('utf-8')
    print(i)

print(5)
# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.
import subprocess
import chardet

def ping_checker(host):

    args = ['ping', host]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

ping_checker('google.com')
ping_checker('yandex.ru')

print(6)
# Создать текстовый файл test_file.txt.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое
with open('test_file.txt.txt', 'r') as t:
    print(t.encoding)
with open('test_file.txt.txt', 'r', encoding='utf-8') as t:
    print(t.readlines())
