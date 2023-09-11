# Problem URL: https://projecteuler.net/problem=854

import multiprocessing

def generate_primes(limit):
    """Generate a list of prime numbers up to the given limit."""
    sieve = [True] * (limit + 1)
    primes = []
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return primes


def pisano_period_length(n, prime):
    """Find the length of the Pisano period for n modulo a prime number."""
    a, b = 0, 1
    period = 0
    while True:
        a, b = b, (a + b) % prime
        period += 1
        if a == 0 and b == 1:
            return period


def find_largest_n_for_pisano(p, primes):
    """Find the largest n such that the Pisano period for n is p."""
    result = 1
    for prime in primes:
        if prime > p:
            break
        period_length = pisano_period_length(prime - 1, prime)
        if period_length == p:
            result = prime - 1
    return result

def find_largest_n_for_pisano_wrapper(args):
    p, primes = args
    return find_largest_n_for_pisano(p, primes)

def calculate_product_P(n, modulo):
    primes = generate_primes(n)
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    args_list = [(p, primes) for p in range(1, n + 1)]
    results = pool.map(find_largest_n_for_pisano_wrapper, args_list)
    pool.close()
    pool.join()

    product = 1
    for result in results:
        product *= result
        product %= modulo
    return product


result = calculate_product_P(1000000, 1234567891)
print(result)

