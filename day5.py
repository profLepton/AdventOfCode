with open("inputs/day5.txt", "r") as f:
    data = f.read().split("\n\n")

line0 = data[0].split(":")[1].lstrip().split(" ")

seeds = [range(int(line0[i]), int(line0[i]) + int(line0[i+1])) for i in range(0, len(line0), 2)]

for block in data[1:]:
    
    interim = []
    
    for line in block.split("\n")[1:]:
        if line == "":
            continue
        dest, src, delta = list(map(int, line.split(" ")))
        
        src_range = range(src, src + delta)
        dest_range = range(dest, dest + delta)

        deleted = []
        replaced = []

        for seed in seeds:
            
            intersection = range(max(seed.start, src_range.start), min(seed.stop, src_range.stop))

            
            
            if len(intersection) > 0:
                deleted.append(seed)

                replaced_candidate1 = range(seed.start, src_range.start)
                replaced_candidate2 = range(src_range.stop, seed.stop)



                if len(replaced_candidate1) > 0:

                    replaced.append(replaced_candidate1)
                if len(replaced_candidate2) > 0:
 
                    replaced.append(replaced_candidate2)

                interim.append(range(dest_range.start + intersection.start - src_range.start, dest_range.start + intersection.stop - src_range.start))


        for seed in deleted:
            seeds.remove(seed)

        for seed in replaced:
            seeds.append(seed)



    if len(interim) > 0:
        seeds.extend(interim)

print(min(seeds, key=lambda x: x.start).start)

            
            



