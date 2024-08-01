
import os
import random
import W
print("Current Directory Contents:", os.listdir('.'))
try:
    word_list = W.word_list
    print("Word list imported successfully.")
except AttributeError:
    print("Failed to import word_list from Words module.")
chosen_word=random.choice(word_list)
print('''888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P" ''')


display=[]
for letter in chosen_word:
    display+="_"

print('''
     _______
     |/      |
     |      (_)
     |       |
     |       |
     |       
     |
 jgs_|___''')
count=0

while  display.__contains__("_") or count<len(chosen_word):
    print(display)
    if not display.__contains__("_"):
        print("Heyy You won the Game Congrats")
        print(f"you have guessed all the letters for the word {chosen_word}")
        print(display)
        break
    found=False
    guess_letter=input("Guess a letter\n").lower()
    for i in range(len(chosen_word)):
        if(chosen_word[i]==guess_letter):
            display[i]=chosen_word[i]
            found=True
    #print(f"found  is {found}")
    if found==False:
        count+=1          
    #print(f"count is {count}")
            
    if count==1:
        print('''       _______
                        |/      |
                        |      (_)
                        |       |
                        |       |
                        |       
                        |
                    jgs_|___
''')
        print("This is your first Wrong word be cautious the next time or you will be hanged till death:\n")
    elif count==2:
        print('''       _______
                        |/      |
                        |      (_)
                        |       |
                        |       |
                        |       
                        |
                    jgs_|___
''')   
        print("This is your Second Wrong word be cautious the next time or you will be hanged till death:\n") 
    elif count==3:
        print('''       _______
                        |/      |
                        |      (_)
                        |      /|/
                        |       |
                        |      
                        |
                    jgs_|___
''')    
        print("This is your Third Wrong word be cautious the next time or you will be hanged till death:\n") 
    elif count==4:
        print('''       _______
                        |/      |
                        |      (_)
                        |      /|/
                        |       |
                    #   |      / /
                        |
                    jgs_|___
                            ''')   
        print("Heyy You Lost the Game ")
        print(f"you haven't guessed all the letters for the word {chosen_word}")
        break
        
clr=input("Do you want to clear the screen \n")
if clr.lower=="yes":
    os.system("cls")
               


        

    