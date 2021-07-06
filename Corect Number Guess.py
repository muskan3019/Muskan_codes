# no. of guesses 5
# print no. of guesses left
# game over
n=45
print("Strat your game now !")
print("note- You can guess the number 5 times, and you want to guess between(1,100)")
print()
limit=0
while limit<5:
    guess = int(input("Enter guess number "))
    limit = limit+1
    if guess==n:
        print("you are won")
        print(f'you could guess the no in {limit} times')
        print(f'You have left number of chances is {5-limit}')
        break
    if guess in range(1,40):
        print("You are guessing less from actual number ")
        print(f'You have left number of chances is {5-limit}')
    if guess in range(50,101):
        print("You are guessing grater from actual number ")
        print(f'You have left number of chances is {5-limit}')
    if guess in range(40,45):
        print("You are too close with actual number")
        print(f'You have left number of chances is {5-limit}')
    if guess in range(46,50):
        print("You are too close with actual number")
        print(f'You have left number of chances is {5-limit}')
if guess!=n:
    print("Game Over")
