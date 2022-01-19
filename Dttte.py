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
if gwin==True:  ###Computer Choose tie
    compt='D'
elif gwin==False: ####computer choose D
    compt='T'
elif gwin==None: ###Computer choose T
    compts='Tie'
  ############line space
#num1 = input("Enter your eecahrge amaount")# first variable
#num2 = input("enter your bet amount" )
#num3=(2)
#This line throw error
you=input("your bet  side:\n(1) for Dragon choose (D)\n (2)for tiger choose(T)\n (3)for Tie choose (Tie)")
def gamed(compt,you):
   if compt==you:
       return True # for wiin condition
   elif compt!=you:
       return False #For Loose condition
   elif compts !=you or compts==you:
       return None #for tie Condition
q=gamed(compt,you)
if q==True:
    print("Well done","The winner is",compt,"\nYou choose =",you)
    print("The card of Dragon is:",d_1,"The card of Tiger is ",t_2)
elif q==False:
    print("Poor predicton\n Try hard to improve","\nThe bet side of you is =",you)
    print("The card of Dragon is:",d_1,"The card of Tiger is ",t_2)
elif q==None:
    print("Match is tie")
    print("The card of Dragon is:",d_1,"The card of Tiger is ",t_2)
