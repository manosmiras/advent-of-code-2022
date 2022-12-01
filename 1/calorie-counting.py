def generate_calorie_list(lines):
    total_calories = 0;
    list = []
    for line in lines:
        if not line:
            list.append(total_calories)
            total_calories = 0;
        else:
            total_calories += int(line)
    list.sort(reverse=True)
    return list;

file = open("input.txt", "r")
data = file.read();
lines = data.splitlines()
print("Elf with most calories: ", generate_calorie_list(lines)[0])
print("Top three elf calories: ", sum(generate_calorie_list(lines)[0:3]))
file.close()