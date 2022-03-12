import numpy as np

def main():
    n, x, y = map(int, input().split())
    print(int(n/x) + int(n/y) - int(n/np.lcm(x, y)))


if __name__ == '__main__':
    main()
