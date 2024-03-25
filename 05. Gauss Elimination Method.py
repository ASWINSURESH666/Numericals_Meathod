def gauss_elimination(matrix):
    n = len(matrix)

    for i in range(n):
      pivot=matrix[i][i]

      for j in range(n):
        if j != i:
          eq=matrix[j][i]/pivot

          for k in range(n+1):
            matrix[j][k] -= eq * matrix[i][k]

      pivot=matrix[i][i]
      for j in range(n+1):
        matrix[i][j] /= pivot

matrix = [[2,2,1,6],
            [4,2,3,4],
            [1,1,1,0]]

gauss_elimination(matrix)

n = len(matrix)
for i in range(n):
  print("x", i+1, "=",matrix[i][-1])
