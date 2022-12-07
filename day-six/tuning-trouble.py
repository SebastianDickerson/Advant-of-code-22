import sys

def is_dupe(packet):
    p_set = set(packet)
    return len(p_set) != len(packet)

packet_marker = 4
message_marker = 14
start_of_packet = 0
start_of_message = 0
start_idx = 0
end_idx = 4
message_end_idx = 14

line = sys.stdin.readline()

for i, char in enumerate(line):
    temp_packet = line[start_idx:end_idx]
    temp_message = line[start_idx:message_end_idx]
    
    # check for duplicates  
    dupe_p = is_dupe(temp_packet)
    dupe_m = is_dupe(temp_message)

    # set the packet marker if duplicate is found in list
    if not dupe_p and start_of_packet == 0: 
        start_of_packet = i + packet_marker

    if not dupe_m and start_of_message == 0:
        start_of_message = i + message_marker
    
    start_idx += 1
    end_idx += 1
    message_end_idx += 1

# part one & part two
print(f"Part one: {start_of_packet}, Part two: {start_of_message}")