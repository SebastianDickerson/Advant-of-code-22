import sys

def is_dupe(packet):
    p_set = set(packet)
    if len(p_set) == len(packet):
        return False
    return True

marker = 4
message_marker = 14
temp_packet = []
temp_message = []
start_of_packet = 0
start_of_message = 0
count = 1
start_idx = 0
end_idx = 4
message_end_idx = 14

line = sys.stdin.readline()

for i, char in enumerate(line):
    for c in line[start_idx:end_idx]:
        temp_packet.append(c)

    for m in line[start_idx:message_end_idx]:
        temp_message.append(m)
    
    # check for duplicates  
    dupe_p = is_dupe(temp_packet)
    dupe_m = is_dupe(temp_message)

    # set the packet marker if duplicate is found in list
    if dupe_p:
        temp_packet.clear()
    elif start_of_packet == 0:
        start_of_packet = i + marker

    if dupe_m:
        temp_message.clear()
    elif start_of_message == 0:
        start_of_message = i + message_marker
    
    start_idx += 1
    end_idx += 1
    message_end_idx += 1

# part one
print(start_of_packet)
# part two
print(start_of_message)