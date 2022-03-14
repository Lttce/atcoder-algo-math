# 011 - Print Prime Numbers

def main():
    n = int(input())

    print(' '.join(map(str, eratosthenes_sieve(n))))


def eratosthenes_sieve(n: int) -> list:
    primes_list = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(n+1):
        if not is_prime[i]:
            continue
        primes_list.append(i)
        for j in range(i*i, n+1, i):
            is_prime[j] = False

    return primes_list


if __name__ == '__main__':
    main()
