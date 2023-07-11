def findZigZagSequence(a, n):
    a.sort()
    print(a)
    mid = int((n + 1) / 2)
    print(a[mid])
    a[mid], a[n - 1] = a[n - 1], a[mid]

    print(mid, a[mid], a[n - 1])

    start = mid + 1
    end = n - 1
    while start < end:  # Corrected the condition from "start <= ed" to "start < ed"
        a[start], a[end] = a[end], a[start]
        start = start + 1
        end = end - 1  # Corrected the increment from "ed = ed + 1" to "ed = ed - 1"

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")


a = [2, 3, 5, 1, 4]
n = len(a)
findZigZagSequence(a, n)
