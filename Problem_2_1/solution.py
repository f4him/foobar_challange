def solution(xs):
    maxNeg = -9999999
    count = 0
    countNeg = 0
    res = str(int(1))

    if len(xs) > 50 or len(xs) < 1 or max(xs) > 1000 or min(xs) < -1000:
        raise ValueError('invalid inputs')

    if len(xs) == 1:
        return str(xs[0])

    for v in xs:
        if v == 0:
            continue

        count += 1
        if v < 0:
            countNeg += 1
            if maxNeg < v:
                maxNeg = v

        res = str(int(res) * v)

    if countNeg == 1 and count == 1:
        return "0"

    if countNeg % 2 == 1:
        res = str(int(int(res) / maxNeg))

    return res if count > 0 else "0"
    

print(solution([2, -3, -4, -5]))
print(solution([2, -3, 1, 0, -5]))
print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))

# My test cases
print(solution([0, 0]))
print(solution([-4]))
print(solution([1, 0]))