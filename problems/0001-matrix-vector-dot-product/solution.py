def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if not a or any(len(row) != len(b) for row in a):
        return -1

    result = []
    for row in a:
        dot_product = sum(row[i] * b[i] for i in range(len(b)))
        result.append(dot_product)

    return result