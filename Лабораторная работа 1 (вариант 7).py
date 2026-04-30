#ЕМЕЛЬЯНЕНКО АНАСТАСИЯ
#ВАРИАНТ 7
#ПЕРВЫЙ ЗАКОН МЕНДЕЛЯ

k, m, n = 2, 2, 2 #сюда вводим три натуральных числа
total = k + m + n
recessive = 0.0
if n >= 2:
    recessive += (n / total) * ((n - 1) / (total - 1))
if m >= 1 and n >= 1:
    recessive += (m / total) * (n / (total - 1)) * 0.5
    recessive += (n / total) * (m / (total - 1)) * 0.5
if m >= 2:
    recessive += (m / total) * ((m - 1) / (total - 1)) * 0.25
dominant = 1 - recessive
a= round(dominant, 5)
print(f"Входные данные: {k} {m} {n}")
print(f"Вероятность доминантного фенотипа: {a}")

with open('mendel_first_law.py', 'w', encoding='utf-8') as file:
    file.write('''#ЕМЕЛЬЯНЕНКО АНАСТАСИЯ
#ВАРИАНТ 7
#ПЕРВЫЙ ЗАКОН МЕНДЕЛЯ

k, m, n = 2, 2, 2
total = k + m + n
recessive = 0.0

if n >= 2:
    recessive += (n / total) * ((n - 1) / (total - 1))
if m >= 1 and n >= 1:
    recessive += (m / total) * (n / (total - 1)) * 0.5
    recessive += (n / total) * (m / (total - 1)) * 0.5
if m >= 2:
    recessive += (m / total) * ((m - 1) / (total - 1)) * 0.25

dominant = 1 - recessive
a = round(dominant, 5)
print(f"Входные данные: {k} {m} {n}")
print(f"Вероятность доминантного фенотипа: {a}")
''')
