def solution(N, M, K):
    sum = 0

    M = sorted(M, reverse=True)
    a = int(N/(K+1))*K  + N%(K+1)
    b = int(N/(K+1))

    sum = a*M[0] + b*M[1]

    print(sum)
    return sum



solution(5, [1,2,4,5,7], 3)
