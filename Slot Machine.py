print ("How much money do you want to start with? ")
Bankinput = input ("")
Bank = Bankinput
while int(Bank) > 0:
    Betinput = input ('How much money do you want to bet? ')
    Bet = int(Betinput)
    Bank = int(Bank) - Bet
    import random
    number1 = random.randint(0, 4)
    number2 = random.randint(0, 4)
    number3 = random.randint(0, 4)
    Thing = [] 
    Thing.append('World Peace')
    Thing.append('Star')
    Thing.append('Family')
    Thing.append('Coal')
    Thing.append('Food')
    print (Thing[number1]+ ' ' + Thing[number2]+ ' '  + Thing[number3])
    if number1 == number2 and number1 == number3 and number1 == 2: 
        Betwin = Bet * 100
        if number1 == number2 and number1 == number3:
            print ('Winner Winner Chicken Dinner')
            Betwin2 = Betwin * 10
            print ('You won $' + str(Betwin2) )
            Bank = Bank + Betwin2
    if number1 == number2 and number1 == number3 and number1 == 3:
        Betwin = Bet / 1000
        print ('You were naughty this year!')
        if number1 == number2 and number1 == number3:
                print ('Winner Winner Chicken Dinner')
                Betwin2 = Betwin * 10
                print ('You won $' + str(Betwin2) )
                Bank = Bank + Betwin2
    if number1 == number2 and number1 == number3 and number1 == 4:
        Betwin = Bet * 10
        if number1 == number2 and number1 == number3:
            print ('Winner Winner Chicken Dinner')
            Betwin2 = Betwin * 10
            print ('You won $' + str(Betwin2) )
            Bank = Bank + Betwin2
    if number1 == number2 and number1 == number3:
        print ('Winner Winner Chicken Dinner')
        Betwin2 = Betwin * 10
        print ('You won $' + str(Betwin2) )
        Bank = Bank + Betwin2
    else:
        print ('Sorry you lost this round.')
    print ('You have $'+ str(Bank) + " in your bank account.")
print ('You lost this game.')
print ('Play again?')
