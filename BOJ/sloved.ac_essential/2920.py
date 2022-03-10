arr = list(map(int, input().split()))
arr_a = arr[:]
arr_d = arr[:]
arr_a.sort()
arr_d.sort(reverse=True)
if arr == arr_a:
    print("ascending")
elif arr == arr_d:
    print("descending")
else:
    print("mixed")