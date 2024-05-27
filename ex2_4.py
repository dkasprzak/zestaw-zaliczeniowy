import multiprocessing
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes

def find_twin_primes(primes):
    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twin_primes.append((primes[i], primes[i + 1]))
    return twin_primes

def worker(start, end):
    primes = find_primes_in_range(start, end)
    twin_primes = find_twin_primes(primes)
    return twin_primes

def main():
    range_start = 2
    range_end = 100000

    num_processes = multiprocessing.cpu_count()

    chunk_size = (range_end - range_start) // num_processes
    ranges = [(range_start + i * chunk_size, range_start + (i + 1) * chunk_size) for i in range(num_processes)]
    ranges[-1] = (ranges[-1][0], range_end)

    pool = multiprocessing.Pool(processes=num_processes)

    results = pool.starmap(worker, ranges)

    all_twin_primes = []
    for result in results:
        all_twin_primes.extend(result)

    for twin_prime in all_twin_primes:
        print(twin_prime)

if __name__ == "__main__":
    main()
