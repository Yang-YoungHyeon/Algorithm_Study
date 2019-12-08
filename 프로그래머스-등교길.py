from math import factorial

def solution(m, n, puddles):
    M = n+1
    N = m+1
    answer = 0

    dp = [[0]*(M) for i in range(N)]
        
    if(puddles == [[]]):
        answer = factorial(m+n-2)/(factorial(n-1)*factorial(m-1))
        return answer% 1000000007

    for puddle in puddles:
        dp[puddle[0]][puddle[1]] = -1

    dp[0][1] = 1


    i = 1
    j = 1
    while(i < N):
        j=1
        while(j < M):
            if(dp[i][j] == -1):
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            j = j+1
        i = i+1
        
    answer = dp[m][n]
    return answer


print(solution(4,3,[[2,2]]));
