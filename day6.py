import math
with open("inputs/day6.txt", "r") as f:
    data = f.read().splitlines()


race_time = int(data[0].split(":")[1].lstrip().replace(" ", ""))

race_distance = int(data[1].split(":")[1].lstrip().replace(" ", ""))

score = 1


D = (race_time**2 - (4*race_distance))**0.5

r1 = (race_time + D) / 2
r2 = (race_time - D) / 2

if math.ceil(r2) == r2:
    r2 = int(r2 + 1)
else:
    r2 = math.ceil(r2)

if math.floor(r1) == r1:
    r1 = int(r1 - 1)

else:
    r1 = math.floor(r1)



score *= len(range(r2, r1+1))

print(score)
    

    


