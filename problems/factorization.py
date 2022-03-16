# 014 - Factorization

def main():
    print(*prime_factorization(int(input())))


def prime_factorization(n: int) -> list:
    prime_factor = []
    div = 2
    while div**2 <= n:
        if n % div == 0:
            prime_factor.append(div)
            n //= div
            continue
        div += 1
    prime_factor.append(n)
    return prime_factor


if __name__ == '__main__':
    main()
