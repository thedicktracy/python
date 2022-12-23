# CabreraP1
# Programmer: Robert Cabrera
# EMail: rcabrera14@cnm.edu
# Purpose: provide user capability to find fruit in a string

#import required modules and libraries
from random import Random
import random

#Function header for this particular assignment
def header():
        print("This function will print a summary explaining the purpose of the program.")
        print("CabreraP1")
        print("Programmer: Robert Cabrera")
        print("EMail: rcabrera14@cnm.edu")
        print("This is a game of rock paper scissor")

#call header function        
header()    

#game function :code and logic
def RPSgame():
    cont = "yes" #continue choice
    c,p,t,cr,pr=0,0,0,0,0  #game counters
    while c < 2 and p < 2 and cont == "yes": #if game limit hasn't been reached and if player wants to keep playing , run through the game logic again
        rps = ["rock", "paper", "scissors"]
        compMove = random.choice(rps)
        
        #for testing
        #print("computer chose :: "+compMove)
        myMove = input("Please select your choice (rock, paper, scissors):: ")
        while myMove != "rock" and myMove != "paper" and myMove != "scissors":
            myMove = input("Please select your choice (rock, paper, scissors):: ")
        print("you chose :: " +myMove)
        #for play
        print("computer chose :: "+compMove)
        
        #game logic
        if compMove == myMove:
            print("you tied")
            t=t+1
        elif compMove == "rock":
            if myMove == "scissors":
                print("computer wins this round")
                c = c+1
            else:
                print("you win this round")
                p=p+1
        elif compMove == "scissors":
            if myMove == "paper":
                print("computer wins this round")
                c=c+1
            else:
                print("you win this round")
                p=p+1
        else:
            if myMove == "rock":
                print("computer wins this round")
                c=c+1  
            else:
                print("you win this round")
                p=p+1
        #final game logic        
        if c==2:
            cr = cr+1
            print("computer wins best 2 out of 3!")
            print("\nPlayer rounds won  ::  ",pr)
            print("Compter rounds won  ::  ",cr,"\n" )
            cont = input("would you like to play again (yes or no) :: ") 
            while cont != "yes" and cont !="no":
                    print("\nplease type yes or no\n")
                    cont = input("would you like to play again (yes or no) :: ")
            if cont == "yes":
                p,c =0,0
            elif cont == "no":
                return
        elif p==2:
            pr=pr+1
            print("you win best 2 out of 3!!")
            print("\nPlayer rounds won  ::  ",pr)
            print("Compter rounds won  ::  ",cr,"\n" )
            cont = input("would you like to play again (yes or no) :: ") 
            while cont != "yes" and cont !="no":
                    print("\nplease type yes or no\n")
                    cont = input("would you like to play again (yes or no) :: ")
            if cont == "yes":
                p,c =0,0
            elif cont == "no":
                return
            
        
        if cont == "no":
            print("the computer won ",cr," rounds !" )
            print("you won ", pr , " rounds !!")
            print("there were ",t,"ties")      
                        
RPSgame()


def Goodbye():
    print("goodbye")
    
Goodbye()