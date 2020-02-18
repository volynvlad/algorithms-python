def robot(N):
    A = [[1] * N for _ in range(N)]
    A[0][0] = 1
    for j in range(1, N):
        for i in range(2, N):
            A[i][j] = A[i - 1][j] + A[i][j - 1]

    for row in A:
        print(row)

    return A[-1][-1]


print(robot(5))
print("-" * 20)
print(robot(10))
