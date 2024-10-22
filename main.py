# Programmer: Andrew Leimbach
# Course:  CS151, Dr. Zee
# Due Date: 10/23/2024
# PA: 02
# Problem Statement:  Runs and displays game of sticks, allowing two players to play with a computer
# Data In: Total sticks, individual player stick choices, Continuation choice
# Data Out:  Instructions, Total sticks remaining, Players losses
# Credits: Class Project

#This program allows two players to play a game of sticks with a computer, creating a total of three players!
#Enter the total number of sticks you'd like to play with and then start taking away sticks at your choice!
#The person who takes the last stick loses!

import random
#Define function
def play_game():
    play_again = True
    losses_player1 = 0
    losses_player2 = 0
    losses_computer = 0

    while play_again:
        # Get the initial number of sticks
        initial_sticks = int(input("Enter the number of sticks (10-100): "))
        while initial_sticks < 10 or initial_sticks > 100:
            print("Invalid input. Try again!")
            initial_sticks = int(input("Enter the number of sticks (10-100): "))

        total_sticks = initial_sticks
        current_player = 1  # 1 for player 1, 2 for player 2, 3 for computer

        # Game loop
        while total_sticks > 0:
            print(f"Sticks remaining: {total_sticks}")

            if current_player == 1:
                num_sticks = int(input("Player 1, enter number of sticks to take (1-3): "))
                while num_sticks < 1 or num_sticks > 3 or num_sticks > total_sticks:
                    print("Invalid input. Try again.")
                    num_sticks = int(input("Player 1, enter number of sticks to take (1-3): "))

            elif current_player == 2:
                num_sticks = int(input("Player 2, enter number of sticks to take (1-3): "))
                while num_sticks < 1 or num_sticks > 3 or num_sticks > total_sticks:
                    print("Invalid input. Try again.")
                    num_sticks = int(input("Player 2, enter number of sticks to take (1-3): "))

            else:  # Computer's turn
                if total_sticks == 2:
                    num_sticks = random.randint(1, 2)
                elif total_sticks == 1:
                    num_sticks = 1
                else:
                    num_sticks = random.randint(1, 3)
                print(f"Computer takes {num_sticks} sticks.")

            total_sticks -= num_sticks

            # Check for loss
            if total_sticks == 0:
                if current_player == 1:
                    losses_player1 += 1
                    print("Player 1 loses!")
                elif current_player == 2:
                    losses_player2 += 1
                    print("Player 2 loses!")
                else:
                    losses_computer += 1
                    print("Computer loses!")

            # Switch player
            current_player = (current_player % 3) + 1

        # Play again prompt
        user_response = input("Do you want to play again? (yes/no): ").strip().lower()
        while user_response not in ['yes', 'no']:
            print("Invalid input. Try again.")
            user_response = input("Do you want to play again? (yes/no): ").strip().lower()

        if user_response == 'yes':
            play_again = True
        else:
            play_again = False
            print(f"Final scores:\nPlayer 1 losses: {losses_player1}\nPlayer 2 losses: {losses_player2}\nComputer losses: {losses_computer}")

play_game()

