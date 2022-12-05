import string

def get_priority(item_type):
    alphabet = list(string.ascii_letters)
    num_list = [n + 1 for n in range(52)]
    priorities = dict(zip(alphabet, num_list))

    return priorities.get(item_type)

def half_string(s):
    s_one = s[:len(s) // 2]
    s_two = s[len(s) // 2:] 
    return s_one, s_two

def match_char(group):
    set_one = set(group[0])
    set_two = set(group[1])
    set_three = set(group[2])

    for char in set_one:
        if set(char).intersection(set_two, set_three):
            return char
    return "no match"

with open('data/raw-data.txt') as file:
    priorities_list = []
    group_list = []
    group_priorities_list = []
    temp_group = []

    lines = file.read().split('\n')

    for line in lines:
        compart_one, compart_two = half_string(line)
        temp_group.append(line)

        if len(temp_group) == 3:
            group_list.append(temp_group[:])
            temp_group.clear()

        for item_one in compart_one:
            for item_two in compart_two:
                if item_two == item_one:
                    priorities_list.append(get_priority(item_two))
                    break
            if item_two == item_one:
                break
    
    for group in group_list:
        char = match_char(group)
        group_priorities_list.append(get_priority((char)))
  
    sum_of_priorities = sum(priorities_list)
    sum_group_priorities_list = sum(group_priorities_list)

    print(sum_group_priorities_list)
    print(sum_of_priorities)
          



