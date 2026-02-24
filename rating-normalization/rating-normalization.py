def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here
    for i in range(len(matrix)):
        sum = 0
        cnt = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                sum += matrix[i][j]
                cnt += 1
        if cnt == 0:
            continue
        mean = float(sum / cnt)
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                matrix[i][j] = matrix[i][j] - mean
    return matrix