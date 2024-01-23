print("Welcome to rock, paper and scissors!")
print("You can play as many rounds as you want.")
print("To end the game, press 0(zero)")
print("Following are the rules of playing the game:")
print("- rock beats scissors")
print("- scissors beat paper")
print("- paper beats rock")
print("Let's play! Press any key to get started!!")
input()
import numpy as np
end = False
player_points = 0
comp_points = 0
while end != True:
    print("Your turn:")
    p_turn = int(input("Please choose any among rock(1), paper(2) or scissors(3):"))
    c_turn = np.random.randint(1,3)
    if c_turn == 1:  #when computer chooses rock
        print("Computer chose rock")       
        if p_turn == 1:  #if player chooses rock as well
            print("It's a draw. ")
            player_points+=1
            comp_points+=1
        elif p_turn == 2:   #if player chooses paper
            print("You won!")            
            player_points+=1
        elif p_turn == 3:    #if player chooses scissors
            print("You loose! :(")
            comp_points+=1
    elif c_turn == 2:   #when computer chooses paper
        print("Computer chose paper")       
        if p_turn == 1:  #if player chooses rock
            print("You loose! :(")
            comp_points+=1
        elif p_turn == 2:   #if player chooses paper as well
            print("It's a draw. ")
            player_points+=1
            comp_points+=1 
        elif p_turn == 3:    #if player chooses scissors
            print("You won!")            
            player_points+=1
    elif c_turn == 3:   #when computer chooses scissors
        print("Computer chose scissors")       
        if p_turn == 1:  #if player chooses rock 
            print("You won!")            
            player_points+=1
        elif p_turn == 2:   #if player chooses paper
            print("You loose! :(")
            comp_points+=1
        elif p_turn == 3:    #if player chooses scissors as well
            print("It's a draw. ")
            player_points+=1
            comp_points+=1 
            
    choice = input("Do you want to continue playing? Y/N ")
    if choice == "Y" or choice == "y":
        end = False
    else:
        end = True

if comp_points < player_points:
    print("Congratulations!! You won with {} points!!".format(player_points))
elif comp_points > player_points:
    print("Oops! You lost. Computer won with {} points.".format(comp_points))
else:
    print("It's a draw.")
