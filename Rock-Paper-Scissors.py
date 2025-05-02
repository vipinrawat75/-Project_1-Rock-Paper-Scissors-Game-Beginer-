'''
rock = 1
paper = 2
scissor = 3
'''
import random

system = random.choice([1, 2, 3])
player = input("rock, paper, sciccor?: ")
num_mean = {"r" : 1, "p" : 2, "s" : 3}        
reverse_num_mean = {1 : "rock", 2 : "paper", 3 : "scissor"}       
player_output = num_mean[player]          

# Explain Result
print(f"you choose: {reverse_num_mean[player_output]}\nComputer choose: {reverse_num_mean[system]}")

if system == player_output:
    print("its a draw")

else:
    if system - player_output == -1 or 2:      
        print("you win")
    else:
        print("you lose")

    if system ==1 and player_output == 2:  
        print("you win!")
    elif system ==1 and player_output == 3:   
        print("you lose!")


    if system ==2 and player_output == 1:    
        print("you lose!")
    elif system ==2 and player_output == 3:  
        print("you win!")


    if system ==3 and player_output == 1:   
        print("you win!")
    elif system ==3 and player_output == 2:    
        print("you lose!")