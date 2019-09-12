# the derivative of cx^2 + k is
# 2cx
# Newton Raphson says that given a guess g for a root,
# g - (2cg^2 + k)/2cg is a better guess


epsilson = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(guess**2 - y) >= epsilson:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2 * guess))
print('numGuesses = ', numGuesses)
print('The square root  of ', y, ' is about ', guess)
