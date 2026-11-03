def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    rows = len(a)
    cols = len(a[0]) if a else 0

    new_rows, new_cols = new_shape

    if rows * cols != new_rows * new_cols:
        return []

    flat = []
    for row in a:
        for num in row:
            flat.append(num)

    reshaped_matrix = []
    index = 0

    for i in range(new_rows):
        new_row = []
        for j in range(new_cols):
            new_row.append(flat[index])
            index += 1
        reshaped_matrix.append(new_row)

    return reshaped_matrix
	