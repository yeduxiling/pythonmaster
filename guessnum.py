import random, sys
n = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
i = 0
while True:
    i += 1
    answer = int(input('Take a guess:'))
    if n > answer:
        print('Your guess is too low.')
    elif n < answer:
        print('Your guess is too high.')
    else:
        print(f'Good job! You guessed my number in {i} guesses!')
        sys.exit()
