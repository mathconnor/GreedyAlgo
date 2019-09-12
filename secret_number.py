print("Please think of a number between 0 and 100!")
low = 0
high = 100
ans = int((high + low)/2)
correct_num = 91

# input(f"Is your secret number {int(ans)}? ")

while True:
    guess = input("Is your secret number " + str(ans) + "?\n"
                    + "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess == 'h':
        high = ans
        ans = int((high + low)/2)
    elif guess == 'l':
        low = ans
        ans = int((high + low)/2)
    elif guess == 'c':
        print("Game over. Your secret number was: ", ans)
        break
    else:
        print("Sorry, I did not understand your input.")




