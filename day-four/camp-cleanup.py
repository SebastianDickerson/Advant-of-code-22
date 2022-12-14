def match_pairs(option, a, b):
    return option(item in a for item in b) or option(item in b for item in a)

with open('data/raw-data.txt') as f:
    lines = f.read().splitlines() 
    all_matched_pairs = []
    any_matched_pairs = []

    for line in lines:
        pairs = line.split(',')
        f_pair = [pair.split('-') for pair in pairs]
        first_elf = [item for item in range(int(f_pair[0][0]), int(f_pair[0][1]) + 1)]
        second_elf = [item for item in range(int(f_pair[1][0]), int(f_pair[1][1]) + 1)]

        if match_pairs(all, first_elf, second_elf):
            all_matched_pairs.append(line)
        
        if match_pairs(any, first_elf, second_elf):
            any_matched_pairs.append(line)
            
    # part 1
    print(len(all_matched_pairs))
    # part 2
    print(len(any_matched_pairs))