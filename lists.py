testList = [1, -4, 8, -9]


# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])
#
# def timesFive(a):
#     return a * 5

# applyToEach(testList, timesFive)
# print(testList)

# def addOne(a):
#     return a + 1
# applyToEach(testList, addOne)
# print(testList)

# def squared(a):
#     return a**2
# applyToEach(testList, squared)
# print(testList)

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):
    return a * a


def halve(a):
    return a / 2


def inc(a):
    return a + 1


print(applyEachTo([inc, halve, square, abs], -3))
