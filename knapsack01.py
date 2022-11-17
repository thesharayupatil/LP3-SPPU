def solution(capacity, wt, profit, no_of_itms):
    DP = [[0 for _ in range(capacity + 1)] for _ in range(no_of_itms + 1)]
    for i in range(no_of_itms + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
             DP[i][j] = 0
            elif wt[i - 1] <= j:
                DP[i][j] = max(profit[i - 1] + DP[i-1][j - wt[i-1]], DP[i - 1][j])
            else:
                DP[i][j] = DP[i-1][j]
    print("The maximum profit is: ", DP[no_of_itms][capacity])
val = [50,100,150,200]
wt = [8,16,32,40]
W = 64
n = len(val)
solution(W, wt, val, n)