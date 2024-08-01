#write a function with three print statements 
def greet():
    print("Hi How are you doing!")
    print("i am doing good!")
    print("what are you upto!")

greet()


#Write a function and call the parameters in the section
def greetWithVar(name,age,dob):
    print(f"Hi My name is {name}")
    print(f"and my age is {age}")
    print(f"my date of birth is {dob}")
   

greetWithVar(name="Rahul",age=25,dob="30th Sep 1996")

#Ceasar's Cipher
import string

lowercase_alphabet=string.ascii_lowercase
print(lowercase_alphabet)

def encode(inputText,Shiftby):
    message=""
    inputText=inputText.lower()
    for i in inputText: 
        index=lowercase_alphabet.find(i)
        if index+Shiftby>25:
            index=(index+Shiftby)-26
            message+=lowercase_alphabet[index]
        else:
            index=index+Shiftby
            message+=lowercase_alphabet[index]
    print(f"The encoded message is {message}")                

def decode(inputText,Shiftby):
    message=""
    inputText=inputText.lower()
    for i in inputText: 
        index=lowercase_alphabet.find(i)
        if index-Shiftby<0:
            index=26-(-(index-Shiftby))
            message+=lowercase_alphabet[index]
        else:
            index=index-Shiftby
            message+=lowercase_alphabet[index]
    print(f"The decoded message is {message}")  
            
                
direction=input("Enter whether you want to encrypt or decrypt a message type E for encoding and D for decoding\n")
if (direction.lower()=="d" or direction.lower()=="e"):
    pass
else:
    while True:
        direction=input("Enter whether you want to encrypt or decrypt a message type E for encoding and D for decoding\n")
        if (direction.lower()=="d" or direction.lower()=="e"):
            break
shift=int(input("please input the number you want to shift your alphabets by\n"))
while shift>26 or shift<0:
    shift=int(input("please input the number you want to shift your alphabets by between 0 to 26\n"))


if direction.lower()=="e":
    text=input("Enter the text you want to encode\n")
    encode(inputText=text,Shiftby=shift)
elif direction.lower()=="d":
    text=input("Enter the text you want to DECODE   \n")
    decode(inputText=text,Shiftby=shift)


