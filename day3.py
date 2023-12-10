with open("inputs/day3.txt", "r") as f:
    data = f.read().splitlines()


def get_number(row, column):
    num = []
    i = column
    max_i = len(data[row])

    if not data[row][i].isnumeric():
        return 0

    while i >= 1:
        if data[row][i-1].isnumeric():
            i -= 1
        else:
            break
        
    
    while i < max_i and data[row][i].isnumeric() :
        num.append(data[row][i])
        i += 1

    return (int("".join(num)), i-1)

ans = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        
        if data[i][j] == "*":

            parts_list = []

            if i > 0:
                parts_list.append(get_number(i-1, j))
                if j > 0:
                    parts_list.append(get_number(i-1, j-1))
                if j < len(data[i])-1:
                    parts_list.append(get_number(i-1, j+1))

            if i < len(data)-1:
                parts_list.append(get_number(i+1, j))
                if j > 0:
                    parts_list.append(get_number(i+1, j-1))
                if j < len(data[i])-1:
                    parts_list.append(get_number(i+1, j+1))

            if j > 0:
                parts_list.append(get_number(i, j-1))

            if j < len(data[i])-1:
                parts_list.append(get_number(i, j+1))

            # remove duplicates

            parts_list = list(set(parts_list))
            parts_list.remove(0)
            

            if len(parts_list) != 2:
                continue

            ans += parts_list[0][0] * parts_list[1][0]
            


print(ans)