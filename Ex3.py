import numpy as np

try:
    arr = input("Введите элементы массива через пробел: ").split()
    arr = np.array([int(num) for num in arr], dtype=np.byte)
    if arr.min() < 0:
        raise ValueError("Массив должен содержать только положительные числа.")
        sum = arr.sum()
    print(f"Сумма элементов массива: {sum}")
except ValueError as e:
    print(e)