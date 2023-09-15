def expected_score(N):
    # Initialize a 3D DP array to store the expected scores
    dp = [[[0 for _ in range(2 * N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]

    # Base case: When there are no coins left, the expected score is 0
    for score in range(2 * N + 1):
        dp[0][0][score] = score

    # Iterate over all possible states
    for f in range(N + 1):
        for u in range(N + 1):
            for score in range(2 * N, -1, -1):
                if f + u == 0:
                    continue
                fair_prob = (0.5 * (1 + dp[min(f + 1, N)][u][min(score + 1, 2 * N)])) if f > 0 else 0
                unfair_prob = (0.5 * (1 + dp[f][min(u + 1, N)][min(score + 1, 2 * N)])) if u > 0 else 0
                stop_prob = (0.5 * (20 + dp[f][u][max(score - 50, 0)]))
                dp[f][u][score] = max(fair_prob, unfair_prob, stop_prob)

    return dp[0][0][0]

# Calculate S(50) and round it to 6 decimal places
result = expected_score(50)
print(round(result, 6))