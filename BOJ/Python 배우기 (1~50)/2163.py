def solve(n,m):
    return (n - 1) + n * (m - 1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    print(solve(N, M))