#!/usr/bin/python3
"""Coin Change Algorithm.
"""


def makeChange(coins, total):
    """It finds fewest coins needed - reach given total
    with set of different valued coins.
    """
    if total <= 0:
        return 0
    rem_am = total
    coins_counted = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem_am > 0:
        if coin_idx >= n:
            return -1
        if rem_am - sorted_coins[coin_idx] >= 0:
            rem_am -= sorted_coins[coin_idx]
            coins_counted += 1
        else:
            coin_idx += 1
    return coins_counted
