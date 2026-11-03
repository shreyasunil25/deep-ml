def calculate_matrix_mean(matrix: list[list[int | float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    if mode == 'row':
        for row in matrix:
            mean = sum(row) / len(row)
            result.append(mean)

    elif mode == 'column':
        for j in range(cols):
            total = 0

            for i in range(rows):
                total += matrix[i][j]

            mean = total / rows
            result.append(mean)

    return result