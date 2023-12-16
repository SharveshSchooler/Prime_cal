def prime(a):
    for j in range(2, a):
        if (a % j == 0):
            return True

    else:
        return False


def Even(a):
    if a % 2 == 0:
        return True
    else:
        return False


l = [2, 4, 13, 9, 7, 121]
for a in l:
    if prime(a):
        print(a, "Is a composite", end="")
    else:
        print(a, "Is a prime", end="")
    if Even(a):
        print(" and a Even number")
    else:
        print(" and a ODD number")
