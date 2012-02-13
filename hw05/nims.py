#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

stones = 40
stones = int(stones) #sets stones as an integer
print "Number of stones in the pile:",stones
print "Max number of stones per turn: 5"
turn = 0
turn = int(turn)
while stones>0: #loop continues as long as at least one stone remains
    print stones,"stones left. Player",turn%2+1, #add 1 to remainder of current turn, and the result is the current player.
    player=raw_input("[1-5]: ")
    player=int(player) 
    if player <=0 or player >=6: #makes sure user inputs 1-5
        print "Invalid number of stones."
    elif player>stones:
        print "Not enough stones."
    elif player==stones: #if user takes as many stones as there are left, he loses
        turn+=1 #this makes sure that the readout displays the opposite player, the winner
        print "Player",turn%2+1,"wins!!!"
        break
    else:
        stones = stones - player #user entry is subtracted from the stones
        turn+=1  #turn automatically goes up by 1

    
    
    
    
    

