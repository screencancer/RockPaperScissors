import random


def aimove():
    move = random.randint(1,3)
    if move == 1:
        move2 = "rock"
    elif move == 2:
        move2 = "paper"
    else:
        move2 = "scissors"
    return move2


def usermove():
    move = input("Input your move rock paper or scissors\n")
    return move


def calcwin(user, ai):
    user2 = user.upper()
    ai2 = ai.upper()
    if user2 == ai2:
        print(user, "and", ai, "is a draw.")

    if user2 == "ROCK" and ai2 == "SCISSORS":
        print("You win", user, "beats", ai)
    elif ai2 == "PAPER" and user2 == "ROCK":
        print(f"You lose {ai} beats {user}")

    if user2 == "PAPER" and ai2 == "SCISSORS":
        print(f"You lose {ai} beats {user}")
    elif ai2 == "ROCK" and user2 == "PAPER":
        print(f"You win {user} beats {ai}")

    if user2 == "SCISSORS" and ai2 == "ROCK":
        print(f"You lose {ai} beats {user}")
    elif ai2 == "PAPER" and user2 == "SCISSORS":
        print(f"You win {user} beats {ai}")



def main():
    move1 = aimove()
    move2 = usermove()
    calcwin(move2, move1)

main()
