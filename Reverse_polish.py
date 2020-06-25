# Импортирую библиотеки для написания веб-страницы и расчётов.
import cgi
import html
import math
# Пишу текст веб-страницы с формой для ввода выражения в ОПЗ.
print("Content-type:text/html\r\n")
print('<html>')
print('<head>')
print('<title>ОПЗ</title>')
print('</head>')
print('<body text = "AAAA00" bgcolor = "000057">')
print('<h1>Калькулятор выражений в опратной польской нотации</h1>')
print('<p>В привычной для нас форме записи математических выражений')
print('операторы располагаются между операндами,')
print('на которые они воздействуют (например, 2 + 7). </p>')
print('<p>Чтобы указать порядок,')
print('в котором должны быть выполнены операции,')
print(' используются скобки. ')
print('А при отсутствии скобок операции выполняются ')
print('согласно правилам приоритета операторов. ')
print('Такая запись получила название инфисной нотации.</p>')
print('<p>Чтобы упростить задачу разбора таких выражений</br>')
print('в компьютерной программе были придуманы: ')
print('префиксная нотация, ')
print('в которой оператор указывется перед операндами (+ 2 7),</br>')
print('а также постфиксная нотация, ')
print('в которой оператор указывается после операндов (2 7 +). ')
print('Такая форма записи называется также обратной польской записью.</p>')
print('<p>Например, выражение</p>')
print('<p>log<sub>2</sub>(17 + tan(18^3.2 - 172) / e^14)</p>')
print('<p>в ОПЗ будет записано как:</p>')
print('<p>18 3.2 ^ 172 - tan 14 exp / 17 + 2 log</p>')
print('<p>В ОПЗ порядок операций определяется без использования скобок, ')
print('что сокращает запись и упрощает алгоритм вычисления. ')
print('Вычислять выражения в ОПЗ можно последовательно слева направо.</p>')
print("<form action= 'Reverse_polish.py'>")
print("        <input type='text' name='TEXT_1'>")
print("        <input type='submit'>")
print('<p>Введите выражение в ОПЗ (десятичный разделитель - точка)')
print("    </form>")
form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "nothing")
# Разбиваю полученное выражение на список из строк.
z = text1.split()
# Операнды конвертирую в числа, операции считаю.
op = 0
for i in range(len(z)):
    if z[i] == "+":
        op += 1
    elif z[i] == "-":
        op += 1
    elif z[i] == "*":
        op += 1
    elif z[i] == "/":
        op += 1
    elif z[i] == "log":
        op += 1
    elif z[i] == "^":
        op += 1
    elif z[i] == "sin":
        op += 1
    elif z[i] == "tg":
        op += 1
    elif z[i] == "cos":
        op += 1
    elif z[i] == "asin":
        op += 1
    elif z[i] == "atan":
        op += 1
    elif z[i] == "acos":
        op += 1
    elif z[i] == "exp":
        op += 1
    elif z[i] == "ln":
        op += 1
    else:
        z[i] = float(z[i])
# Для каждой операции слева направо рассчитываю промежуточное значение.
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
        elif z[i] == "^":
            z[i] = z[i - 2] ** z[i - 1]
            del z[i - 1]
            del z[i - 2]
            break
        elif z[i] == "sin":
            z[i] = math.sin(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "tg":
            z[i] = math.tan(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "cos":
            z[i] = math.cos(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "ctg":
            z[i] = math.cot(z[i - 1])
            z[i] = 1/z[i]
            del z[i - 1]
            break
        elif z[i] == "asin":
            z[i] = math.asin(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "atg":
            z[i] = math.atan(z[i - 1])
            del z[i - 1]
            break
        elif z[i] == "acos":
            z[i] = math.acos(z[i - 1])
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
# В конце в списке должен остаться один элемент, который является ответом.
print(text1, " = ", z[0])
print('</body>')
print('</html>')
