total_income = 0
count = 0
while True:
    income = float(input())
    if income == 0:
        break
    total_income += income
    count += 1
average_income = total_income / count if count > 0 else 0
print(average_income)
