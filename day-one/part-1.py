def elf_cals(input):
    temp_total = 0
    elf_cals = []

    for idx in range(len(input)):
        if input[idx] != '':
            temp_total += int(input[idx])
        else:
            elf_cals.append(temp_total)
            temp_total = 0

    return elf_cals

with open('data/raw-data.txt') as f:
    lines = f.read().splitlines() 

    cal_totals = elf_cals(lines)
    largest_cal_intake = max(cal_totals)
    top_three_total = sum(sorted(cal_totals, reverse=True)[:3])   

    print(largest_cal_intake)
    print(top_three_total)

    f.close()
