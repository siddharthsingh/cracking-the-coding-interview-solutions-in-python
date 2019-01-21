def rotateMatrix(matrix):
    if not matrix or len(matrix[1])<2:return matrix
    s = 0
    e = len(matrix)-1

    while s<e:
        # print(s,e)
        for i in range(s,e):

            temp,matrix[s + i][e] =matrix[s + i][e], matrix[s][s+i]
            temp,matrix[e][e-i] = matrix[e][e-i],temp
            temp,matrix[e-i][s] = matrix[e-i][s],temp
            matrix[s][s+i] = temp
        s+=1
        e-=1
    return matrix

def rotateMatrix2(matrix):
    if not matrix or len(matrix[1])<2:return matrix
    s = 0
    e = len(matrix)-1

    while s<e:
        # print(s,e)
        for i in range(s,e):

            matrix[s + i][e],matrix[e][e-i],matrix[e-i][s],matrix[s][s+i] =matrix[s][s+i],matrix[s + i][e],matrix[e][e-i],matrix[e-i][s]

        s+=1
        e-=1
    return matrix




matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in range(30000000):
    rotateMatrix2(matrix)
# print(rotateMatrix2(matrix))

