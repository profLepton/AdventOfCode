with open("inputs/day2.txt", "r") as f:
    data = f.read().splitlines()

colors = ["red", "green", "blue"]

max_balls = (12, 13, 14)

ans = 0


for i in data:
    i = i.replace(",", "")
    game_id = i.split(":")[0].split()[1]
    
    game_strings = i[i.find(":")+1:].split(";")

    color_max = [0 for color in colors]
    for game in game_strings:

        game = game.split()
        for k in range(1, len(game), 2):
            for i in range(len(colors)):
                if game[k] == colors[i]:
                    color_max[i] = max(color_max[i], int(game[k-1]))
                    continue

    power = 1
    for i in color_max:
        power *= i

    ans += power

print(ans)