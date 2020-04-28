import random
max_roll=6
def game(pot):
    diceRoll1=random.randrange(1, max_roll)
    diceRoll2=random.randrange(1, max_roll)
    
    if diceRoll1+diceRoll2==7:
        pot=pot+4
    else:
        pot=pot-1
    return pot
def main():
    pot=int(input("Enter: "))
    roll=0
    biggestRoll=0
    biggestPot=pot
    while pot:
        while pot>0:
            pot=game(pot)
            roll+=1
            if pot>biggestPot:
                biggestPot=pot
                biggestRoll=roll
            print(roll, '\t', pot)
        print("It took", roll, "rolls to get bankrupt")
        print("Your biggest pot was", biggestPot, "on roll")
        pot=int(input("Enter: "))
main()
