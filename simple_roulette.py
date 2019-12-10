import random
import sys



def divider():
    print("*********************************************************")


def roulette(balance):
    divider()
    print("Balance:", balance)
    divider()
    x=input("Wählen Sie eine Zahl zwischen 0 und 14 oder rot/schwarz: ")
    divider()
    s=int(input("Wählen Sie ihren Einsatz: "))
    divider()
    while s>balance:
        news=int(input("Ungültiger Einsatz, wählen Sie einen neuen: "))
        if news<=s: s=news
        divider()

    r=random.randint(0,14)

    if r==1 or r==3 or r==5 or r==7 or r==9 or r==11 or r==13:
        print("Es wurde die schwarze",r,"gerollt!")
    elif r==2 or r==4 or r==6 or r==8 or r==10 or r==12 or r==14:
        print("Es wurde die rote",r,"gerollt!")
    else:
        print("Es wurde die grüne 0 gerollte!")
    divider()
    if x=="schwarz" and (r==1 or r==3 or r==5 or r==7 or r==9 or r==11 or r==13):

        print("Sie haben gewonnen!")
        print("New Balance:",balance+s)

        return (balance+s)

    elif x=="rot" and (r==2 or r==4 or r==6 or r==8 or r==10 or r==12 or r==14):

        print("Sie haben gewonnen!")
        print("New Balance:", balance+s)

        return (balance+s)

    elif x=="0" and r==0:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="1" and r==1:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="2" and r==2:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="3" and r==3:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="4" and r==4:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="5" and r==5:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="6" and r==6:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="7" and r==7:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="8" and r==8:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="9" and r==9:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="0" and r==0:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="10" and r==10:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="11" and r==11:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="12" and r==12:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="13" and r==13:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    elif x=="14" and r==14:

        print("Sie haben gewonen!")
        print("New Balance:", balance+(s*14))

        return (balance+(s*14))

    else:
        print("Sie haben verloren!")
        print("New Balance:", balance-s)

        return(balance-s)



def game():
    balance = 1000
    while True:
        if balance == 0:
            divider()
            t=input("Sie sind pleite, wollen Sie mehr Geld einzahlen? (y/n)")
            divider()
            if t=="y":
                tt=int(input("Wie viel wollen Sie einzahlen: "))
                balance+=tt
                divider()
                print("Vielen Dank!")
            else: break

        balance = roulette(balance)

game()