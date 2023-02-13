arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]

for i in range(0, len(arr), 5):
    arr[i:i+2] = arr[i:i+2][::-1]
    arr[i+2:i+5] = arr[i+2:i+5][::-1]

print(arr)
