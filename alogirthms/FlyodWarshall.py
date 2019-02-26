adj_matrix = [
    [0,3,float("inf"),7],
    [8,0,2,float("inf")],
    [5,float("inf"),0,1],
    [2,float("inf"),float("inf"),0],


]


def floyd_warshall(adj_matrix):
    """

    :param adj_matrix:
    :return:
    """
    n = len(adj_matrix)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if adj_matrix[j][k] > adj_matrix[j][i] + adj_matrix[j][i]:
                    adj_matrix[j][k] = adj_matrix[j][i] + adj_matrix[i][k]

floyd_warshall(adj_matrix)
print(adj_matrix)
