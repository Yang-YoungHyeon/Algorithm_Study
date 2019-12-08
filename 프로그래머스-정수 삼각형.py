import copy
def solution(triangle):
    tri = copy.copy(triangle)
    dp = []

    for i in range(len(triangle)):
        dp.append(copy.copy(tri[i]))
        if(i!=0):
            for j in range(i):
                temp = (tri[i][j] + tri[i - 1][j])
                if (dp[i][j] < temp):
                    dp[i][j] = temp
                temp = (tri[i][j + 1] + tri[i - 1][j])
                if (dp[i][j + 1] < temp):
                    dp[i][j + 1] = temp
            tri[i] = dp[i]


    ans = dp[len(dp)-1]
    ans.sort()
    answer = ans.pop()
    return answer

''' 입출력 예시 '''
print(solution([[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]))
