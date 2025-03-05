lst = [1, 1, 2, 3, 4, 5, 5, 5]
max_num = lst[0]
max_count = 1
current_num = lst[0]
current_count = 1

for num in lst[1:]:
    if num == current_num:
        current_count += 1
    else:
        if current_count > max_count:
            max_count = current_count
            max_num = current_num
        current_num = num
        current_count = 1

# Final check for the last group
if current_count > max_count:
    max_count = current_count
    max_num = current_num

print("Longest consecutive repeated number:", max_num, "repeated", max_count, "times")
