# 012 - Primality Test

def main():
    print('Yes' if is_prime(int(input())) else 'No')


def is_prime(n: int) -> bool:
    from math import floor, sqrt
    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
