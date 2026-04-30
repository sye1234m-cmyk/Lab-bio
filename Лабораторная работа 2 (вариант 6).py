# ЕМЕЛЬЯНЕНКО АНАСТАСИЯ
# ЛАБОРАТОРНАЯ РАБОТА 2
# ВАРИАНТ 6
#КОНСЕНСУС И ПРОФИЛИ
file_name = input("Введите имя файла: ")

with open(file_name, 'r') as f:
    lines = f.readlines()

sequences = [] #все строки ДНК
DNA = ""  #для сборки текущей строки ДНК

for line in lines:
    line = line.strip() #для очистки лишних
    if len(line) > 0 and line[0] == '>':
        if DNA:
            sequences.append(DNA)
            DNA = ""
    else:
        DNA += line

if DNA:
    sequences.append(DNA)

if len(sequences) > 10:
    print("Ошибка: количество строк ДНК превышает 10")
    exit()

length = len(sequences[0])
if length > 1000:
    print("Ошибка: длина строки превышает 1000 символов")
    exit()

for seq in sequences:
    if len(seq) != length:
        print("Ошибка: строки имеют разную длину")
        exit()

print(f"Количество строк: {len(sequences)}")
print(f"Длина строк: {length}\n")

count_A = [0] * length
count_C = [0] * length
count_G = [0] * length
count_T = [0] * length

for seq in sequences: #для подсчёта каждого нуклеотида в строке ДНК
    for i in range(length):
        if seq[i] == 'A':
            count_A[i] += 1
        elif seq[i] == 'C':
            count_C[i] += 1
        elif seq[i] == 'G':
            count_G[i] += 1
        elif seq[i] == 'T':
            count_T[i] += 1

consensus = ""
for i in range(length):
    max_count = count_A[i]
    best = 'A'
    if count_C[i] > max_count:
        max_count = count_C[i]
        best = 'C'
    if count_G[i] > max_count:
        max_count = count_G[i]
        best = 'G'
    if count_T[i] > max_count:
        max_count = count_T[i]
        best = 'T'
    consensus += best

print("Консенсусная последовательность:")
print(consensus)
print()
print("Матрица профилей:")
print("A:", ' '.join(map(str, count_A)))
print("C:", ' '.join(map(str, count_C)))
print("G:", ' '.join(map(str, count_G)))
print("T:", ' '.join(map(str, count_T)))
