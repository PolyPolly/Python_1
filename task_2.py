# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, divider=","):
    group_list1 = group1.split(divider)
    group_list2 = group2.split(divider)
    common_participants = list(set(group_list1).intersection(group_list2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
