def task_3(file_name):
    with open(file_name) as f:
        n = int(f.readline())
        numbers = []
        for i in range(n):
            numbers.append(list(map(int, f.readline().split())))
    max_summa = 0



print(task_3("27_hard_a.txt"), task_3("27_hard_b.txt"))
