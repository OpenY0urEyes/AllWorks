from functools import reduce

arr = []
n = int(input("Введите размер массива: "))
for i in range(n):
    arr.append(int(input(f"Введите элемент {i+1}: ")))

max_val = arr[0]
for i in range(1, n):
    if arr[i] > max_val:
        max_val = arr[i]
print(f"Максимальное значение (цикл): {max_val}")

max_val = max(arr)
print(f"Максимальное значение (функция): {max_val}")

min_val = arr[0]
for i in range(1, n):
    if arr[i] < min_val:
        min_val = arr[i]
print(f"Минимальное значение (цикл): {min_val}")

min_val = min(arr)
print(f"Минимальное значение (функция): {min_val}")

avg_val = sum(arr) / n
print(f"Среднее значение: {avg_val}")

x = int(input("Введите искомое значение: "))
index = -1
for i in range(n):
    if arr[i] == x:
        index = i
        break
print(f"Индекс искомого значения: {index}")

count = 0
for i in range(n):
    count += 1
print(f"Количество элементов (цикл): {count}")

count = len(arr)
print(f"Количество элементов (функция): {count}")

sum_val = 0
for i in range(n):
    sum_val += arr[i]
print(f"Сумма значений (цикл): {sum_val}")

sum_val = sum(arr)
print(f"Сумма значений (функция): {sum_val}")

prod_val = 1
for i in range(n):
    prod_val *= arr[i]
print(f"Произведение значений (цикл): {prod_val}")

prod_val = reduce((lambda x, y: x * y), arr)
print(f"Произведение значений (функция): {prod_val}")