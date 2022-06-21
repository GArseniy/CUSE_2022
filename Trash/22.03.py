def is_prime(number):
    if abs(number - round(number)) > 2 * 10 ** -15:
        return False
    number = round(number)
    if (number == 1) or (number == 3):
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def task_1():
    print("Task 1:")
    count = 0
    for number in range(1000000, 5000000):
        count += is_prime(number)
    print(count)


def task_2():
    print("Task 2:")
    for number in range(int(123456789 ** 0.1), int(987654321 ** 0.1) + 1):
        if is_prime(number) and (number ** 10 in range(123456789, 987654321 + 1)):
            print(number ** 10)


def task_3():
    def is_int(a):
        return abs(a - round(a)) <= 2 * 10 ** -15
    print("Task 3:")
    count = 0
    for number in range(1234567, 7654321 + 1):
        degree = 0
        while True:
            if number % (3 ** (degree + 1)) == 0:
                degree += 1
            else:
                break
        p = (number / (3 ** degree)) ** (1 / 6)
        if is_int(p):
            if is_prime(p):
                count += 1
    print(count)


def task_4():
    print("Task 4:")
    count = 0
    for number in range(int((12345678 / 5) ** 0.25), int((87654321 / 5) ** 0.25) + 1):
        if is_prime(number) and (number ** 4 * 5 in range(12345678, 87654321 + 1)):
            count += 1
    print(count)


def task_5():
    print("Task 5:")
    # number = p1 ** a1  *  p2 ** a2  *  ...  *  pn ** an
    # count(dividers) = (a1 + 1)*(a2 + 1)*...*(an + 1) = 256 = 2 ** 8
    # p = [2, 3, 5, 7, 11, 13, 17, 19]
    # a = [0, 0, 0, 0, 0, 0, 0, 0]
    # n = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    # * 4 better than * 19
    # * 16 better than * 17
    # * 9 better than * 16
    n = 2 * 3 * 5 * 7 * 11 * 13 * 4 * 9
    print(n)
