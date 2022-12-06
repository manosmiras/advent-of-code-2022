def get_range_from_pair(pair):
    pair = pair.split("-")
    return range(int(pair[0]), int(pair[1]) + 1)

def fully_overlap(range1, range2):
    if range1 and range2:
        if set(range1).issubset(set(range2)):
            return True
        elif set(range2).issubset(set(range1)):
            return True
    return False

def overlap(range1, range2):
    return [e for e in range1 if e in range2]

def get_fully_overlapping_assignment_count(assignments):
    fully_overlapping_count = 0
    for assignment in assignments:
        assignment_pairs = assignment.split(",")
        first_pair = get_range_from_pair(assignment_pairs[0])
        second_pair = get_range_from_pair(assignment_pairs[1])
        full_overlap = fully_overlap([*first_pair], [*second_pair])
        if full_overlap:
            fully_overlapping_count += 1
    return fully_overlapping_count

def get_overlapping_assignment_count(assignments):
    overlapping_count = 0
    for assignment in assignments:
        assignment_pairs = assignment.split(",")
        first_pair = get_range_from_pair(assignment_pairs[0])
        second_pair = get_range_from_pair(assignment_pairs[1])
        full_overlap = overlap([*first_pair], [*second_pair])
        if full_overlap:
            overlapping_count += 1
    return overlapping_count

file = open("input.txt", "r")
data = file.read()
assignments = data.splitlines()
print(get_fully_overlapping_assignment_count(assignments))
print(get_overlapping_assignment_count(assignments))
file.close()