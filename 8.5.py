def is_perfect(num):
    return sum(i for i in range(1, num) if num % i == 0) == num

n = int(input("Введите число N: "))
perfect_count = sum(1 for i in range(2, n + 1) if is_perfect(i))
print(perfect_count)
