import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    A = np.array(vectors)

    C = np.cov(A)

    return C.tolist()