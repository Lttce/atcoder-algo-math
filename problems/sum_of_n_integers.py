from sys import stdin


def main():
    input = stdin.readline

    _ = int(input())
    print(sum(list(map(int, input().split()))))


if __name__ == '__main__':
    main()
