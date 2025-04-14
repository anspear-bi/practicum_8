best_score = 0
friends_count = 0
while True:
    score = int(input())
    if score == -1:
        break
    if score > best_score:
        best_score = score
    friends_count += 1
print(f'Количество друзей: {friends_count}')
