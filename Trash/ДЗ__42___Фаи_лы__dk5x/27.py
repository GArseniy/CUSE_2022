def task_10(file_name):
    numbers = []
    with open(file_name) as f:
        n = int(f.readline())
        for i in range(n):
            numbers.append(list(map(int, f.readline().split())))
    max_sum = 0
    min_diff4 = 10000000000
    for couple in numbers:
        max_sum += max(couple)
        if (max(couple) - min(couple)) % 4:
            min_diff4 = min(min_diff4, max(couple) - min(couple))
    if max_sum % 4:
        return max_sum
    return max_sum - min_diff4


print(task_10("27_dz_a.txt"), task_10("27_dz_b.txt"))
