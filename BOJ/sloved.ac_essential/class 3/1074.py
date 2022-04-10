N, r, c = map(int, input().split())
start = 0
end = 4 ** N - 1
while True:
    quar = (end - start + 1) // 4
    pivot = (2 ** N) // 2
    if r < pivot and c < pivot:
        end -= 3 * quar
    elif (r < pivot and c >= pivot):
        c -= pivot
        start += quar
        end -= 2 * quar
    elif (r >= pivot and c < pivot):
        r -= pivot
        start += 2 * quar
        end -= quar
    else:
        r -= pivot
        c -= pivot
        start += 3 * quar
    if N == 0:
        break
    N -= 1

print(start)