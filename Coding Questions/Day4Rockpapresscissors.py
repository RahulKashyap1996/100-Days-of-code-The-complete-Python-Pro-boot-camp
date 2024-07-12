import random
import sys

rock='''            _    
                              88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a 
'''
paper='''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88
'''

scissors='''
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P'
'''
#print(rock,paper,scissors)

choice=int(input("What do you choose ? Type 0 for Rock, 1 for Paper and 2 for scissors\n"))
#print(type(choice))
if choice==0:
    print(f"You chose: Rock")
    print(rock)
elif(choice==1):
    print(f"You chose: Paper")
    print(paper)
elif(choice==2):
    print(f"You chose: Scissors")
    print(scissors)
else:
    print("Please choose the correct option from 0 and 1 and 2")    
    


choice1=random.randint(0,2)
if choice1==0:
    print(f"Computer chose: Rock")
    print(rock)
elif(choice1==1):
    print(f"Computer chose: Paper")
    print(paper)
elif(choice1==2):
    print(f"Computer chose: Scissors")
    print(scissors)

if choice==choice1:
    print("No one wins play again:")
elif choice==0 and choice1==1:
    print("Computer Wins!")
elif choice==1 and choice1==2:
    print("Computer wins")
elif choice==0 and choice1==2:
    print("You Win")
else:
    print("you Win")            

