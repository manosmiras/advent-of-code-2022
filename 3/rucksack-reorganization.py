import string
import numpy as np
priority_list = string.ascii_lowercase + string.ascii_uppercase
def get_priority_of_common_items(things):
    common_item = set(things[0])
    for x in range(1, len(things)):
        common_item &= set(things[x])
    # print(common_item)
    return priority_list.find(list(common_item)[0]) + 1

def get_sum_p1(rucksacks):
    sum = 0
    for rucksack in rucksacks:
        first_compartment, second_compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        sum += get_priority_of_common_items([first_compartment, second_compartment])
    return sum

def get_sum_p2(rucksacks):
    sum = 0
    rucksacks_by_group = np.array_split(rucksacks, len(rucksacks)/3)
    for rucksack_group in rucksacks_by_group:
        sum+= get_priority_of_common_items(rucksack_group)
    return sum

file = open("input.txt", "r")
data = file.read()
rucksacks = data.splitlines()
print(get_sum_p1(rucksacks))
print(get_sum_p2(rucksacks))