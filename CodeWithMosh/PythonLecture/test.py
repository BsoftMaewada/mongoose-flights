

def solution(A):
    rows = []
    for arr in A:
        result =- 1
        for num in range (len(rows)):
            if arr < rows[num]:
                result = num
        if result !=- 1:
            rows[result] = arr
        else:
            rows.append(arr)
    return len(rows)
pass

print("Number of Rows: ", solution(range(1, 10000)))

def solution(A):
    sum = 0
    n = len(A)
    for a in A:
        sum += a
    sol = ([True]* (sum + 1) * (n - 1))
    
    for i in range(1, sum):
        sol[0][i] = False
        
    for i in range(1, n):
        for j in range(1, sum):
            sol[i][j] = sol[i -1][j]
            if A [j-1] <= j:
                sol[i][j] != sol[i -1][j-A[i-1]]
                
    min = int()
    j = int(sum/2)
    
    while j >= 0:
        if sol[n][j] == True:
            min = sum - 2*j
            break
        j = j - 1
    return min