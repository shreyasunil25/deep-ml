import math

def calculate_eigenvalues(matrix: list[list[int | float]]) -> list[float]:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    trace = a + d
    determinant = a * d - b * c

    discriminant = trace**2 - 4 * determinant

    if discriminant < 0:
        return []

    eigenvalue1 = (trace + math.sqrt(discriminant)) / 2
    eigenvalue2 = (trace - math.sqrt(discriminant)) / 2

    return sorted([eigenvalue1, eigenvalue2], reverse=True)