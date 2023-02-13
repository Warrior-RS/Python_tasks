#Given array [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o].

#You must reverse first 2 elements of the array, then 3, then 2, then 3, and so on, until the end

#The result: [b, a, e, d, c, g, f, j, i, h, l, k, o, n, m]





















arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]

for i in range(0, len(arr), 5):
    arr[i:i+2] = arr[i:i+2][::-1]
    arr[i+2:i+5] = arr[i+2:i+5][::-1]

print(arr)
