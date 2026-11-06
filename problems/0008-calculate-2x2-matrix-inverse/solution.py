import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    # n=len(matrix)
    # m=len(matrix[0])
    # det=(matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    # if n!=2 or m!=2 or det==0:
    #     return None
    
    # A=[[0,0],[0,0]]
    
    # A[0][0]=matrix[1][1]/det
    # A[1][1]=matrix[0][0]/det
    # A[0][1]=-matrix[0][1]/det
    # A[1][0]=-matrix[1][0]/det

    # return A
    A = np.array(matrix)

    if A.shape != (2, 2):
        return None

    det = np.linalg.det(A)

    if det== 0:
        return None

    return np.linalg.inv(A).tolist()


