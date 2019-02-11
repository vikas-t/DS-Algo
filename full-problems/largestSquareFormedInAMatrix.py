def solNaive(mat, n, m):
    left = [[0 for _ in range(m)] for _ in range(n)]
    up =   [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        # Create an array which contains the length of continuous 
        # ones to its left
        for j in range(m):
            if j == 0:
                left[i][j] = mat[i][j]
                continue
            if mat[i][j] == 1:
                left[i][j] = left[i][j-1] + 1
    
    for i in range(n):
        # Create an array which contains the length of continuous 
        # ones in upwards direction
        for j in range(m):
            if i == 0:
                up[i][j] = mat[i][j]
                continue
            if mat[i][j] == 1:
                up[i][j] = up[i-1][j] + 1

    mx = 0
    for i in range(n):
        for j in range(m):
            l = min(left[i][j], up[i][j])
            for tl in range(l, 0, -1):
            # Traverse one by one so that we keep checking that we
            # know how far we can go with the all ones
                if not left[i-tl+1][j] >= tl or not up[i][j-tl+1] >= tl:
                    mx = max(mx, tl-1)
                    break
                mx = max(mx, tl)
                # If the condition inside is not met, we update with the max
                # tl
    return mx


def sol(mat, n, m):
    subMat = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        subMat[i][0] = mat[i][0]
        
    for i in range(m):
        subMat[0][i] = mat[0][i]
    
    mx = 0
    for i in range(n):
        for j in range(m):
            # We start with 0 and not 1 to handle the cases if there is only
            # one row or only one column
            if i > 0 and j > 0:
                if mat[i][j] == 1:
                    subMat[i][j] = min(subMat[i-1][j], subMat[i][j-1], subMat[i-1][j-1]) + 1
                else:
                    subMat[i][j] = 0
            mx = max(subMat[i][j], mx)
            
    return mx

n, m  = 5, 6
arr = list(map(int, "0 1 0 1 0 1 1 0 1 0 1 0 0 1 1 1 1 0 0 0 1 1 1 0 1 1 1 1 1 1".split()))
mat = [[0 for _ in range(m)] for _  in range(n)]
k = 0
for i in range(n):
    for j in range(m):
        mat[i][j] = arr[k]
        k+=1
print(sol(mat, n, m))