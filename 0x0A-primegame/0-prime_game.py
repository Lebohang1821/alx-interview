#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    # Function to generate a list of primes up to max_n using Sieve of Eratosthenes
    def sieve_of_eratosthenes(limit):
        is_prime = [True] * (limit + 1)
        p = 2
        while (p * p <= limit):
            if (is_prime[p] == True):
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = []
        for p in range(2, limit + 1):
            if is_prime[p]:
                prime_numbers.append(p)
        return prime_numbers
    
    # Determine winner for each round
    def determine_round_winner(n):
        if n < 2:
            return None  # No prime numbers to pick
        
        # Get all prime numbers up to n using sieve of Eratosthenes
        primes = sieve_of_eratosthenes(n)
        
        # Initialize availability of numbers
        available = [True] * (n + 1)
        available[0] = available[1] = False  # 0 and 1 are not prime
        
        # Mark multiples of each prime number as unavailable
        for p in primes:
            if p > n:
                break
            for multiple in range(p, n + 1, p):
                available[multiple] = False
        
        maria_turn = True
        while True:
            found_move = False
            # Maria starts from 2 upwards to n
            for num in range(2, n + 1):
                if available[num]:
                    found_move = True
                    n = num  # New n after removing num and its multiples
                    available[num] = False
                    break
            if not found_move:
                break
            maria_turn = not maria_turn
        
        if maria_turn:
            return 'Ben'  # Maria couldn't make a move, so Ben wins
        else:
            return 'Maria'  # Ben couldn't make a move, so Maria wins
    
    # Determine overall winner across all rounds
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = determine_round_winner(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None  # If the winner cannot be determined

# Example usage:
print(isWinner(5, [2, 5, 1, 4, 3]))
