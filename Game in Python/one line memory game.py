'''
Subject: One Line Memory Game using python . "version 1"
Author: Mohamed Ahmed Abd Elquawy Abd Elghani .
Date : 30/5/2022. "Last modification"
'''
import random
matches1=['A','B','C','D','E','F','G','H','I','J']
matches=2*matches1  #List that won't be shown to user.
random.shuffle (matches)  # Changing the positions of items in the list randomly .
user_matches=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #List that will be shown to user.
print("WELCOME to the memory game! \n ",user_matches)
p1_s=0 #player one score
p2_s=0 #player two score
import os # function that will clear the screen after each turn .
from time import sleep 
def screen_clear():
    if os.name=='posix':
        _=os.system('clear')
    else:
        _=os.system('cls')
   
while(user_matches!=['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']):
        print("player1 turn \n ",user_matches)
        in1=float(input("Please Enter a frist number from the list above \n"))
        while(in1 not in user_matches): #Prevent the player from entering a wrong input.
            in1=float(input("Wrong choice!!! Please Enter a frist number from the list above \n"))
        in2=float(input("Please Enter a second number from the list above \n")) 
        while (in2 not in user_matches): #Prevent the player from entering a wrong
            in2=float(input("Wrong choice!!! Please Enter a second number from the list above \n"))
        while(in1==in2): #Prevent the player from entering the same input.
            in2=float(input("Wrong choice!!! Please enter a different number \n"))
        user_matches[int(in1)-1]=matches[int(in1)-1] 
        user_matches[int(in2)-1]=matches[int(in2)-1] 
        #Replacing the player's choices with thier corspondings in the other list.
        print(user_matches , '\n')
        #checking if the choices are same or not. 
        if(user_matches[int(in1)-1]==user_matches[int(in2)-1]):
            user_matches[int(in1)-1]=user_matches[int(in2)-1]=matches[int(in1)-1]=matches[int(in2)-1]="*"
            p1_s=p1_s + 1 # increasing the player score.
            print ("player1 score =",p1_s,'\n',"player2 score = ",p2_s,'\n',user_matches,'\n')
        else:
            # returning the original list.
            user_matches[int(in1)-1]=int(in1)
            user_matches[int(in2)-1]=int(in2)
            print("player1 score =",p1_s,'\n',"player2 score = ",p2_s,'\n')
        sleep(5)
        screen_clear() #calling the clear screen function.
        print("player2 turn \n",user_matches)
        in3=float(input("Enter a first number from the list above \n"))
        while(in3 not in user_matches ): #Prevent the player from entering a wrong input.
            in3=float(input("Wrong choice!!! Please Enter a frist number from the list above \n"))  
        in4=float(input("Enter a second number from the list above \n"))
        while(in4 not in user_matches): #Prevent the player from entering a wrong input.
            in4=float(input("Wrong choice!!! Please Enter a second number from the list above \n"))
        while(in4==in3): #Prevent the player from entering the same input.
            in4=float(input("Wrong choice!!! Please enter a different number \n"))
        user_matches[int(in3)-1]=matches[int(in3)-1]
        user_matches[int(in4)-1]=matches[int(in4)-1]
        #Replacing the player's choices with thier corspondings in the other list.
        print(user_matches)
        #checking if the choices are same or not. 
        if(user_matches[int(in3)-1]==user_matches[int(in4)-1]):
            user_matches[int(in3)-1]=user_matches[int(in4)-1]=matches[int(in3)-1]=matches[int(in4)-1]='*'
            p2_s=p2_s+ 1  # increasing the player score.
            print ("player1 score =",p1_s,'\n',"player2 score = ",p2_s,'\n')
        else:
            # returning the original list.
            user_matches[int(in3)-1]=int(in3)
            user_matches[int(in4)-1]=int(in4)
            print("player1 score =",p1_s,'\n',"player2 score = ",p2_s,'\n')
        sleep(5)
        screen_clear() # calling the clear screen function
#Cheking if the game is draw or someone wins.
if(p1_s>p2_s):
    print("Congratulations ,player one wins!!!")
elif(p1_s==p2_s):
    print("The result is Draw")
elif(p1_s<p2_s):
    print("Congratulations ,player 2 wins!!!")
