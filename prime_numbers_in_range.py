"""
Script to print all prime numbers in a given interval.
Demonstrates loop structures, conditionals, and boolean flags.
"""

def get_primes_in_range(start: int, end: int) -> list:
    """
    Returns a list of prime numbers between start and end (inclusive).
    """
    primes = []
    
    for num in range(start, end + 1):
        # Prime numbers are greater than 1
        if num > 1:
            is_prime = True
            # Iterate up to the square root of num for efficiency
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            
            if is_prime:
                primes.append(num)
                
    return primes
