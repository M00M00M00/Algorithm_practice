def main():
    arr = list(map(int,input().split()))
    arr.sort()
    N = int(input())
    a = 0
    b = 1
    for _ in range(N):
        a += 1
        b += 2
        in_arr = list(map(int, input().split()))
        for i in in_arr:
            arr.append(i)
        arr.sort()
        print(arr[a], arr[b])

if __name__=="__main__":
    main()