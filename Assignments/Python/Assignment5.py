#Assignment-5
#w.a.p to play Stone,Paper,Scissor with Computer



import random
def print_menu():
    print("Enter 1 to choose Stone")
    print("Enter 2 to choose paper")
    print("Enter 3 to choose Scissor")

def scores(user,comp):
    print("---Scores---")
    print("User:",user)
    print("Computer:",comp)
    print("------------")




print("Welcome to Stone|Paper|Scissor")
a = int(input("Enter 1 to play: "))
print(a)

user=0
comp=0
choice=True
while (choice):
    print_menu()
    ch = int(input())
    c = random.randint(1,3)
    if (ch==1 and c==1):
        print("I choose Stone")
        print("It's a draw")
        scores(user,comp)
    elif (ch==1 and c==2):
        print("I choose Paper")
        comp+=1
        print("Yes!!! I win this round")
        scores(user,comp)
    elif (ch==1 and c==3):
        print("I choose Scissor")
        user+=1
        print("Uggh!! I lost this round")
        scores(user,comp)
    elif (ch==2 and c==1):
        print("I choose Stone")
        user+=1
        print("Uggh!! I lost this round")
        scores(user,comp)
    elif (ch==2 and c==2):
        print("I choose Paper")
        print("It's a draw")
        scores(user,comp)
    elif (ch==2 and c==3):
        print("I choose Scissor")
        comp+=1
        print("Yes!!! I win this round")
        scores(user,comp)
    elif (ch==3 and c==1):
        print("I choose Stone")
        comp+=1
        print("Yes!!! I win this round")
        scores(user,comp)
    elif (ch==3 and c==2):
        print("I choose Paper")
        user+=1
        print("Uggh!! I lost this round")
        scores(user,comp)
    elif (ch==3 and c==3):
        print("I choose Scissor")
        print("It's a draw")
        scores(user,comp)
    else:
        print("Please enter valid input")
    if (user==5 or comp==5):
        if user==5:
            print("You won the match, I'll see you next time.")
            break
        else:
            print("I won the match, I'll see you next time.")
            break


    
    
        
