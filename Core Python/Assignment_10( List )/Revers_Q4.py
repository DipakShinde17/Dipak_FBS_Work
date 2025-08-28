
my_list = [1, 2, 3, 90,8,6,8,4, 5]
reversed_list = []

for i in range(len(my_list)-1, -1, -1):
    reversed_list.append(my_list[i])

print("Reversed list:", reversed_list)