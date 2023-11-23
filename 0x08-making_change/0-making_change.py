#!/usr/bin/python3
""" making change file"""


def makeChange(coins, total):
    """Given a pile of coins of different values
    determine the fewest number of coins needed to meet a given amount total
    """
    if total < 0:
        return 0
    # Initialize an array to store the minimum number of coins
    # needed for each total from 0 to the given total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins needed to make change for zero total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
