# 008 - Brute Force 1

def main():
    n, s = map(int, input().split())

    count = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a+b <= s:
                count += 1

    print(count)


if __name__ == '__main__':
    main()
