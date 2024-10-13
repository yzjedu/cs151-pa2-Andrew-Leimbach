# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully
1. Set play_again = true
2. Set losses_player1 = 0
3. Set losses_player2 = 0
4. Set losses_computer = 0
2. While play_again == true
1. Prompt user to enter number of sticks (10-100)
2. While initial_sticks < 10 or initial_sticks > 100:
   1. Output "Invalid input. Try again!"
   2. Prompt user to enter intial_sticks again
3. Set total_sticks = initial_sticks
4. Set current_player = 1 (1-player 1, 2-player 2, 3-computer)
5. While total_sticks > 0 
   1. Output sticks remaining
   2. If current_player == 1
      1. Prompt player 1 to enter number of sticks (1-3)
      2. While num_sticks < 1 or num_sticks or num_sticks > total_sticks
         1. Output "Invalid input. Try again."
         2. Prompt again for num_sticks
   3. Otherwise if current_player == 2
      1. Prompt player 2 to enter number of sticks (1-3)
      2. While chosen_sticks < 1 or num_sticks > 3 or num_sticks > total_sticks
         1. Output "Invalid input. Try again."
         2. Prompt again for num_sticks
   4. Otherwise
      3. num_sticks = random.randint(1, 3)
      4. If num_sticks > total_sticks
         5. num_sticks = total_sticks - 1
         6. Output computers sticks taken
   5. Subtract num_sticks from total_sticks
   6. If total_sticks == 0 
      1. If current_player == 1
         1. losses_player1 +=1
         2. Output Player 1 Losses
      2. Otherwise if current_player == 2
         1. losses_player2 +=1
         2. Output Player 2 Losses
      3. Otherwise
         1. losses-computer +=1
         2. Output Computers losses
6. Prompt user to play again (yes or no)
7. While user_response != 'yes' and user_response != "no"
   1. Output "Invalid input. Try again."
   2. Prompt user to try again
8. If user_response == 'yes'
   1. Set play_again = true
9. Otherwise 
   1. play_again = false
10. Output final scores