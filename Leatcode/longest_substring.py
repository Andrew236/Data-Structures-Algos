def longest_sub_string(s):
    curr_index = 0
    place_index = 0
    longest = []
    local_count = 0
    count = 0
    while place_index < len(s):
        if s[place_index] not in longest:
            longest.append(s[place_index])
            local_count += 1
            place_index += 1
            if count < local_count:
                count = local_count
        else:
            curr_index += 1
            if len(longest) == 1:
                local_count = 0
                place_index = curr_index
                longest.clear()
            else:
                local_count = 0
                place_index = curr_index
                longest.clear()
    return count

print(longest_sub_string("pwwkew"))
