def isEven(i):
    """
    :param i: positive integer
    :return: boolean
    """
    print("hi")
    return i % 2 == 0

print(isEven(3))
isEven(2)


def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)

print(foo(5))