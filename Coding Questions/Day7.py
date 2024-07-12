import random

word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
guess_letter=input("Guess a letter\n").lower()

for i in range(len(chosen_word)):
    if(chosen_word[i]==guess_letter):
        print("Right")
    else:
        print("Wrong")
