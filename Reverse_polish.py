#Импортирую библиотеки для написания веб-страницы и расчётов.Файл должен находиться в папке cgi-bin, которая должна лежать в папке работающего веб-сервера. 
import cgi
import html
import math
#Пишу текст веб-страницы с формой для ввода выражения в ОПЗ (с кнопками не разобрался).
print("Content-type:text/html\r\n")
print('<html>') 
print('<head>')
print('<title>Обратная польская нотация</title>')
print('<meta http-equiv="content-type" content="text/html; charset=windows-1251" />')
print('</head>')
print('<body text = "AAAA00" bgcolor = "000057">')
print('<h1>Обратная польская запись</h1>')
print('<p>В привычной для нас форме записи математических выражений операторы располагаются между операндами, на которые они воздействуют (например, 2 + 7). Чтобы указать порядок, в котором должны быть выполнены операции, используются скобки. А при отсутствии скобок операции выполняются согласно правилам приоритета операторов. Такая запись получила название инфисной нотации.</p>')
print('<p>Чтобы упростить задачу разбора таких выражений были придуманы префиксная нотация, в которой оператор указывется перед операндами (+ 2 7), а также постфиксная нотация, в которой оператор указывается после операторов. Такая форма записи называется также обратной польской записью (ОПЗ).</p>')
print('<p>Например, выражение</p>')
print('<p>log2(17 + tan(18^3.2 - 172) / e^14)</p>')
print('<p>в ОПЗ будет записано как:</p>')
print('<p>18 3.2 ** 172 – tan 14 exp / 17 + 2 log</p>')
print('<p>В ОПЗ порядок операций определяется без использования скобок, что сокращает запись и упрощает алгоритм вычисления. Вычислять выражения в ОПЗ можно последовательно слева направо.</p>')
print("<form action= 'Reverse_polish.py'>")
print("        <input type='text' name='TEXT_1'>")
print("        <input type='submit'>")
print("    </form>")
form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "nothing")
#Разбиваю полученное выражение на список из строк.
z = text1.split()
#Операнды конвертирую в числа, операции считаю.
op = 0
for i in range(len(z)):
    if z[i] == "+" or z[i] == "-" or z[i] == "*" or z[i] == "/" or z[i] == "log" or z[i] == "**" or z[i] == "sin" or z[i] == "tan" or z[i] == "cos" or z[i] == "cot" or z[i] == "asin" or z[i] == "atan" or z[i] == "acos" or z[i] == "acot" or z[i] == "exp" or z[i] == "ln":
        op += 1
    else:
        z[i] = float(z[i])
#Для каждой операции слева направо рассчитываю промежуточное значение, оставляю его в спискеж.
for i in range(op):
    for i in range(len(z)):
        if z[i] == "+":
            z[i] = z[i - 1] + z[i - 2]
            del z[i - 1]
            del z[i - 2]
            break
        elif z[i] == "-":
            z[i] = z[i - 2] - z[i - 1]
            del z[i - 1]
            del z[i - 2]
            break
        elif z[i] == "*":
            z[i] = z[i - 1] * z[i - 2]
            del z[i - 1]
            del z[i - 2]
            break
        elif z[i] == "/":
            z[i] = z[i - 2] / z[i - 1]
            del z[i - 1]
            del z[i - 2]
            break
        elif z[i] == "log":
            z[i] = math.log(z[i - 2], z[i - 1])
            del z[i - 1]
            del z[i - 2]
            break
        elif z[i] == "**":
            z[i] = z[i - 2] ** z[i - 1]
            del z[i - 1]
            del z[i - 2]
            break
        elif z[i] == "sin":
            z[i] = math.sin(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "tan":
            z[i] = math.tan(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "cos":
            z[i] = math.cos(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "cot":
            z[i] = math.cot(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "asin":
            z[i] = math.asin(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "atan":
            z[i] = math.atan(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "acos":
            z[i] = math.acos(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "acot":
            z[i] = math.acot(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "exp":
            z[i] = math.exp(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "ln":
            z[i] = math.log1p(z[i - 1])
            del z[i - 1]
            break
#В конце в списке должен остаться один элемент, который является ответом. Никакой реакции на ошибки пользователя не предусмотрено.
print(text1, " = ", z[0])
print('</body>')
print('</html>')