user_inpt=input("Enter your name:")######legends never die
print("Welcome to your programe:",user_inpt)
import random
def gamec(d_1,t_1):
    if d_1==t_2:
        return None ### for making tie condition
    elif d_1>t_2:
        return True #### for making D condition
    elif t_2>d_1: 
        return False  ### for making T condition
d_1=random.randint(1 ,13)
t_2=random.randint(1,13)
gwin=gamec(d_1,t_2)
if gwin==None:  ###Computer Choose tie
    compt='Tie'
elif gwin==True: ####computer choose D
    compt='D'
elif gwin==False: ###Computer choose T
    compt='T'
  ############line space
num1 =int(input("Enter your recharge amount Dear:"))# first variable
num2 =int(input("enter your bet amount Dear:" ))
if num2>num1:
    pass
##if num2>num1:
you=input(" Please choose your bet  side:")
if compt==you:
    z1=(num2)+(num1)####adding 2x balance
    ########print("the balance is ",z1)
    print("Winner is : "           ,compt)
    print ("The card of Dragon is ",d_1,  "AND   The card of Tiger is ",t_2)
    print("You choose right side")
    print("Dear",user_inpt,":Your reaminig coin balance is:",z1)
else:
    z2=(num1)-(num2)
    ####print("the balamce is",z2)
    print("You loose  The winner is ",compt)
    print ("The card of Dragon is ",d_1," AND   the card of Tiger is ",t_2)
    print("You choose wrong side",you)
    print("Dear",user_inpt,":Your remaining balance is:",z2)
    #Legends never die 
    #practise make man perfect