def is_perfect(num):
    return sum(i for i in range(1, num) if num % i == 0) == num
n = int(input("Введите число N: "))
for i in range(2, n + 1):
    if is_perfect(i):
        print(i)
