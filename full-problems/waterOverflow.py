# https://practice.geeksforgeeks.org/problems/champagne-overflow/0

def sol(k, glasses, sr, sg):
    if glasses[sr][sg] + k <= 1:
        glasses[sr][sg] += k
        return
    else:
        spill = glasses[sr][sg] + k - 1
        glasses[sr][sg] = 1
        sol(spill/2, glasses, sr+1, sg)
        sol(spill/2, glasses, sr+1, sg+1)

k=10
i=4
j=1
glasses = [[0]*(i+1) for i in range(k)]
sol(k, glasses, 0, 0)
print("{:.6f}".format(glasses[i-1][j-1]))