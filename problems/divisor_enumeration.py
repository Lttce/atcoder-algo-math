# 013 - Divisor Enumeration

def main():
    print('\n'.join(map(str, divisor_emumeration(int(input())))))


def divisor_emumeration(n: int):
    divisor = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisor.add(i)
            divisor.add(n//i)
    return divisor


if __name__ == '__main__':
    main()
