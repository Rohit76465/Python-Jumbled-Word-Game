import random
def choose():
    z=["rainbow","computer","science","player","water"]
    y=random.choice(z)
    return y

def jumble(picked_word):
    x= " ".join(random.sample(picked_word,len(picked_word)))
    return x

def thank(player1,player2,pointp1,pointp2):
    print(player1,"Your Score is: ",pointp1)
    print(player2, "Your Score is: ", pointp2)
    print("Thanks for playing")
    print("Have a nice day")

def play():
    player1=input("Player1 , Please enter your name")
    player2 = input("Player2 , Please enter your name")
    pointp1=0
    pointp2=0
    turn=0
    c=1
    while(c==1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)

        if(turn%2==0):
            print(player1,"Your turn")
            ans=input("What is the answer ?")
            if(ans==picked_word):
                pointp1=pointp1+1
                print("Your Score is :",pointp1)
            else:
                print("Better Luck Next Time")
                print("The answer is: ",picked_word)
            c=input("Press 1 to Continue or 0 to Quit")
            c=int(c)
            if(c==0):
                thank(player1,player2,pointp1,pointp2)


        else:
            print(player2, "Your turn")
            ans = input("What is the answer ?")
            if (ans == picked_word):
                pointp2 = pointp2 + 1
                print("Your Score is :", pointp2)
            else:
                print("Better Luck Next Time")
                print("The answer is: ", picked_word)
            c = input("Press 1 to Continue or 0 to Quit")
            c = int(c)
            if (c == 0):
                thank(player1, player2, pointp1, pointp2)
                

        turn=turn+1

play()






