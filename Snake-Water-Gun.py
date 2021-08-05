import random

def gameWin(comp,you):

    if comp == you:
        return None

    if comp =='S':
        if you =='W':
            return False
        elif you =='G':
            return True

    elif comp=='W':
        if you == 'G':
            return False
        elif you == 'S':
            return True

    elif comp =='G':
        if you=='S':
            return False
        elif you =='W':
            return True  

print('')            
print('############ -- WELCOME TO SNAKE,WATER,GUN  GAME --#############')      
print('')

print(' START ')
print('')
print('')
you = input("Your Turn: Snake(S) Water(W) or Gun(G)?  :")

print("Comp Turn: Snake(S) Water(W) or Gun(G)  ")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'S'
elif randNo == 2:
    comp = 'W'
elif randNo == 3:
    comp = 'G'

a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")    
