def sort_key(el):
    return el[1]


file_list = ('1.txt', '2.txt', '3.txt')
result_list = []
for file_name in file_list:
    with open(file_name, encoding='utf-8') as f:
        lines = f.readlines()
        result_list.append((file_name, len(lines), lines))
result_list_sorted = sorted(result_list, key=sort_key)

with open('Result.txt', 'a', encoding='utf-8') as f:
    for cort in result_list_sorted:
        f.write(cort[0] + '\n')
        f.write(str(cort[1]) + '\n')
        for line in cort[2]:
            if cort == result_list_sorted[-1] and line == cort[2][-1]:
                f.write(line.strip())
            else:
                f.write(line.strip() + '\n')