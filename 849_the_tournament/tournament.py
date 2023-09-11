def calculate_F(n):
    MOD = 10**9 + 7

    # Initialize a table to store the number of outcomes for each total points value.
    dp = [0] * (n + 1)

    # There is only one possible outcome for n = 2.
    dp[2] = 3

    # Calculate F(n) for n = 3 to n.
    for i in range(3, n + 1):
        # Calculate the number of distinct outcomes for n teams.
        # The number of outcomes is equal to the number of outcomes for (n-1) teams
        # plus the number of outcomes for (n-2) teams, multiplied by 2 (to account for
        # the two possible orderings of the teams in the outcomes).
        dp[i] = (dp[i - 1] + dp[i - 2]) * 2 % MOD

    return dp[n]

# Calculate F(100) modulo 10^9+7
result = calculate_F(100)
print(result)
