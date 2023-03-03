#implement nussinov algorithm to predict secondary structure
def nussinov(seq):
    n = len(seq)
    #initialize matrix
    matrix = np.zeros((n,n))
    #fill matrix
    for i in range(n):
        for j in range(i+4,n):
            #fill in the matrix
            matrix[i,j] = max(matrix[i,j-1], matrix[i+1,j], matrix[i+1,j-1] + s(seq[i],seq[j]), max([matrix[i,k] + matrix[k+1,j] for k in range(i+1,j)]))
    #traceback
    i,j = 0,n-1
    pairs = []
    while i < j:
        if matrix[i,j] == matrix[i+1,j]:
            i += 1
        elif matrix[i,j] == matrix[i,j-1]:
            j -= 1
        elif matrix[i,j] == matrix[i+1,j-1] + s(seq[i],seq[j]):
            pairs.append((i,j))
            i += 1
            j -= 1
        else:
            for k in range(i+1,j):
                if matrix[i,j] == matrix[i,k] + matrix[k+1,j]:
                    pairs.append((k,k+1))
                    i,j = k,k+1
                    break
    return pairs