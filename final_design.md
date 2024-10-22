# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 
1. Set Values:
   1. play_again = true
   3. losses_player1 = 0
   4. losses_player2 = 0
   4. losses_computer = 0

2. While play_again = true:
   1. Prompt user to enter number of sticks(1-100)
   2. While initial sticks < 10 or initial_sticks >100:
      1. Output "Invalid input. Try again!"
      2. Prompt user to enter initial_sticks again
   3. Set total_sticks = initial_sticks 
   4. Set current player = 1 (1-Player 1 , 2-Player 2, 3- Computer)
3. While total_sticks > 0:
   1. Output "Sticks remaining: total_sticks"
   2. If current_player = 1: 
      1. Prompt player 1 to enter number of sticks (1-3)
      2. While num_sticks < 1 or num_sticks > 3 or num_sticks > total_sticks
         1. Output "Invalid input. Try again."
         2. Prompt player 1 again for num_sticks
   3. Otherwise if current_player = 2:
      1. Prompt player 2 to enter number of sticks (1-3)
      2. While num_sticks < 1 or num_sticks > 3 or num_sticks > total_sticks:
         1. Output "Invalid input. Try again."
         2. Prompt player 2 again for num_sticks
   4. Otherwise:
      1. If total_sticks = 2:
         1. Set num_sticks = random.randint(1,2)
      2. Otherwise if total_sticks = 1
         3. num_sticks = 1
      3. Otherwise: 
         1. Set num_sticks = random.randint(1, 3)
      4. Output Computers choice
   5. Subtract num_sticks from total_sticks
   6. If total_sticks = 0
      1. If current_player = 1
         1. Increment losses_player1
         2. Output "Player 1 loses!"
      2. Otherwise if current_player = 2
         1. Increment losses_player2
         2. Output "Player 2 loses!"
      3. Otherwise
         1. Increment losses_computer
         2. Output "Computer loses!"
   7. Set current_player = (current_player % 3) + 1
4. Prompt user to play again (yes or no)
5. While user_response is not 'yes' or user_response is not "no"
   1. Output "Invalid input. Try again."
   2. Prompt user to try again
6. If user_response = 'yes'
   1. Set play_again = true
7. Otherwise
   1. Set play_again = false
   2. Output final scores
      1. Output Player 1 losses
      2. Output Player 2 losses
      3. Output Player 2 losses

I believe this algorithm seems to be mostly right and show the program in a readable essay.
I feel that I might have been able to be more specific, but the other aspects I think I did a good job in.
This algorithm was by far one of the most complicated algorithms I have had to design, so it was nice getting good practice in and facing a harder challenge.
   