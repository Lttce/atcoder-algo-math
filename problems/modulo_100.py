from sys import stdin


def main():
    input = stdin.readline

    _ = int(input())
    print(sum(list(map(int, input().split()))) % 100)


if __name__ == '__main__':
    main()
