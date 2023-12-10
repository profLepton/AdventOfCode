with open("inputs/day4.txt", "r") as f:
    data = f.read().splitlines()

score = 0

data = [(i, 1) for i in data]


for i in range(len(data)):
    copies = data[i][1]
    cards = data[i][0].split(":")[1]
    match_num, win_num = cards.split("|")[0], cards.split("|")[1]
    match_num, win_num = list(map(int, match_num.split())), list(map(int, win_num.split()))


    num_wins = 0
    
    for num in match_num:
        if num in win_num:
            num_wins += 1

    j = i+1

    while j < min(len(data), i+num_wins+1):
        data[j] = (data[j][0], data[j][1]+copies)
        j += 1

    

for i in data:
    print(i)
    score += i[1]

print(score)