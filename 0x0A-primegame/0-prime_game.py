#!/usr/bin/python3
"""Module for Prime Game.
"""


def isWinner(x, nums):
    """It determines winner of prime game session over `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # it generate list of prime statuses up to maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    # It implement Sieve of Eratosthenes to find all primes up to n
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # It filter number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
