import random 
ran= random.randint(1,100)
print ("👋___hello friends ___👋")
print ("welcome to the guessing game")
print ("Here I will choose a number between 1 to 100 and you have guess what is the number is "
)
print ("**note: you have only 10 chances")
def call():
    print ("●●do you want to play again●●")
    s=input("°°hint: y-->yes,n-->no  ==>")
    if s=='y' or s=='Y':
        guess ()
    elif s=='n' or s=='N':
        print ('you left')
    else:
        print ('invalid input')
        print ("please try again ")
        guess ()
def guess():
    
    for i in range(10):    
        m=int (input("Enter your guessing number :"))
        if m==ran:
            print ("        💥congratulations💥")
            print ("****************************************")
            print ("  🤟 you guessed the correct number 🤟")
            print("****************************************")
            break 
        elif m>ran:
            print ("Too large ! try again ")
        elif m<ran:
            print ("Too small ! try again ")
        else:
            print ('invalid input')
        print ("***you have {} chances left***" . format (9-i))
    else:
        print ("sorry! your chances are over")
    call()
guess()
