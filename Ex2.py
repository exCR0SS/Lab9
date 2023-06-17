try:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # пример матрицы
    col_num = int(input("Введите номер столбца: "))
    if col_num < 0 or col_num >= len(matrix[0]):
        raise ValueError("Нет столбца с таким номером.")
    column = [row[col_num] for row in matrix]
    print("Столбец:")
    for num in column:
        print(num)
except ValueError as e:
    print(e)
