#!/usr/bin/python3
"""Coin Change Algorithm.
"""


def makeChange(coins, total):
    """It finds fewest coins needed to reach given total
    with set of different valued coins.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_i
???END
