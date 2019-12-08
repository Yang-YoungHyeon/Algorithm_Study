def solution(N):
    dp = []
    dp.append(4)
    dp.append(6)
    i = 2
    while(i<N):
        dp.append(dp[i-1] + dp[i-2])
        i= i+1
    return dp[N-1]


''' 입출력 예시 '''
print(solution(5))
print(solution(6))
