def countWays(N, memo):
    if N == 0:
        return 1
    elif N <= 2:
        return N

    if N in memo:
        return memo[N]

    
    memo[N] = countWays(N - 1, memo) + countWays(N - 2, memo) + countWays(N - 3, memo)
    return memo[N]

def probabilityOfMissingCeremony(N):
    memo = {}  

    total_ways = countWays(N, memo)


    ways_to_miss_ceremony = countWays(N - 1, memo) + countWays(N - 2, memo) + countWays(N - 3, memo)

    # Represent the answer as a string "Answer of (2) / Answer of (1)"
    answer = f"{ways_to_miss_ceremony}/{total_ways}"
    return answer

# Test cases
print(probabilityOfMissingCeremony(5))  
print(probabilityOfMissingCeremony(10))  