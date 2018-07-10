from random import randint

print('Let us play a game~~')
print('Guess Number~~')

print('Now, I get a number (0,100)')
num = randint(0,100)

print('Can you get it?')
guess = eval(input())
while guess != num:
    if num > guess:
        print('too small!')
    if num < guess:
        print('too big!')
    guess = eval(input())
print('Bingo!')
print('game over, see you next time.');