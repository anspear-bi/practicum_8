for base in [8, 9, 1]:
    for i in range(1, 10):
        sequence = ''.join(str(x) for x in range(1, i + 1))
        result = int(sequence) * base + i
        print(f"{sequence} * {base} + {i} = {result}")
