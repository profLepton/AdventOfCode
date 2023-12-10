with open("inputs/day1.txt", "r") as f:
    data = f.read().splitlines()


digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

ex = "eight3one"
ans = 0
for i in data:
    digit_indices = []
    for j, digit in enumerate(digits):
        if digit in i:
            find1 = i.find(digit)
            find2 = i.rfind(digit)
            digit_indices.append((str(j), find1))
            if find1 != find2:
                digit_indices.append((str(j), find2))

    num_list = [*i]
    num_list = [(i, index) for index, i in enumerate(num_list) if i.isdigit()]
    
    digit_indices.extend(num_list)

    digit_indices.sort(key=lambda x: x[1])

    num = int(digit_indices[0][0] + digit_indices[0][0] if len(digit_indices) == 1 else digit_indices[0][0] + digit_indices[-1][0])
    ans += num


print(ans)


