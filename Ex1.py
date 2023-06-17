try:
    arr = input("Введите элементы массива через пробел: ").split()
    arr = [int(num) for num in arr]
    positive_nums = [num for num in arr if num > 0]
    if len(positive_nums) == 0:
        raise ValueError("В массиве нет положительных чисел.")
    avg = sum(positive_nums) / len(positive_nums)
    print(f"Среднее значение положительных элементов: {avg}")
except ValueError as e:
    print(e)