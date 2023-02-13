def smallest_number_divisible_by_n(n):
    for i in range(1, n + 1):
        if (10 ** i - 1) % n == 0:
            return str(10 ** i - 1)
    return "NO"

n = int(input().strip())
print(smallest_number_divisible_by_n(n))
