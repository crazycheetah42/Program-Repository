import random
print("Welcome to Rock Paper Scissors, Python edition.")
bot_rps_words = ["Rock", "Paper", "Scissors"]
bot_rps = random.choice(bot_rps_words)
print("Bot chooses " + bot_rps)
player_rps = input("Please enter either Rock, Paper, or Scissors: ")
print("Player chooses " + player_rps)
if player_rps == "Rock":
    if bot_rps == "Paper":
        print("Paper beats rock, Bot wins!")
    elif bot_rps == "Rock":
        print("Tie!")
    elif bot_rps == "Scissors":
        print("Rock crushes Scissors, Player wins!")
if player_rps == "Paper":
    if bot_rps == "Rock":
        print("Paper beats Rock, Player wins!")
    elif bot_rps == "Paper":
        print("Tie!")
    elif bot_rps == "Scissors":
        print("Scissors cut paper, Bot wins!")
if player_rps == "Scissors":
    if bot_rps == "Rock":
        print("Rock crushes scissors, Bot wins!")
    elif bot_rps == "Paper":
        print("Scissors cut paper, Player wins!")
    elif bot_rps == "Scissors":
        print("Tie!")