chances = 5
number = input('Type a number from 1-9')
guess = input('Guess Here')


if guess == number:
    print('!!!You Win!!!')

if not guess == number:
    chances = chances-1
    print('Not it Try Again')

if chances == 0:
    print('!!You Lose!!')