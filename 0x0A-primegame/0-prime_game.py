#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the winner of a prime game session over `x` rounds.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int): A list of integers representing the upper bounds
                        of the numbers in each round.

    Returns:
    str: The name of the player with the most wins ('Maria' or 'Ben').
         Returns None if there is a tie or if invalid parameters are provided.
    """
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    # Generate a list of prime statuses up to the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1)]
    primes[0] = False  # 1 is not a prime number

    # Implement Sieve of Eratosthenes to find all primes up to n
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Determine the number of primes less than each number in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
