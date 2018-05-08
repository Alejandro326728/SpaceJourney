import time

print("Welcome to space adventure say Yes to start")
sword = "fists"
shop1=''
food = 0
health = 10
monster1 ="no"
start = input("")
if start == "Yes":
    print("You are going to space!!!! To the moon!!!!")
    money = 5
    print("You start your space adventure with 5 euros")
    time.sleep(2)
    print("first you think to buy food.")
    food1 = input("Do you want to buy food?Yes or No?")
    time.sleep(2)
    if food1 == "Yes":
        money = money - 2
        food = 2
        print("Now you have {} euros and {} of food".format(money, food))
        print("You have {} of health".format(health))
    elif food1 == "No":
        food = 0
        print("Now you have {} euros and {} of food".format(money, food))
    print("You go to the Nasa Rocket Launcher")
    time.sleep(2)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("LAUNCH!!!!!!!")
    print("You start getting hungry")
    if food >= 2:
        print("You eat a can of food")
        food = food - 1
    elif food == 0:
        print("You dont have food, you loose one of health")
        health = health - 1
        print("You have {} of health".format(health))
    time.sleep(2)
    print ("You arrived at the moon!!! you have {} of health and {} euros".format(health,money))
    time.sleep(2)
    print ("Oh NO YOU CRASHED!!!!")
    time.sleep(2)
    escape=input("Do you want to jump of and risk it? Yes or No?")
    if escape=="Yes":
        health= health - 4
        print ("You lost 4 of health.Now you have {} of health".format(health))
    elif escape == "No":
        health = health - 7
        print ("You have {} of health, you were lucky to survive".format(health))
        print ("You hurt yourself during the crash you loose 2 of health")
        health = health - 2
        print ("You have {} of health".format(health))
        if health <= 0:
            print("Game over")
            quit ()
    print("You notice you rae not in the moon")
    time.sleep(2)
    print ("There are 2 coins on the floor")
    collect1=input("Doy you want to pick them up?")
    if collect1=="Yes" or collect1=="yes":
        money = money + 2
        monster1="yes"
        print("you collected the two coins")
        print("You see a beast running at you...")
        time.sleep(2)
        print("Now you see that you shouldent have picked the coins up")
        print("there is a shop next to you")
        time.sleep(2)
        shop1=input("Do you want to buy one of the following?"
                    "Wooden sword/ health pack/nothing? sword= 2 euros health pack = 1 euro you have {} euros. If you buy more that you can afford you die")
        if shop1=="Wooden sword":
            money= money-2
            print("You payed 2 euros")
            sword = "wooden sword"
            if money <=1:
                print ("Game over")
                quit()
        elif shop1=="health pack":
            health=health + 6
            if health >10:
                health = 10
                print("You have {} of health now".format(health))
                money = money -1
                if money <=0:
                    print ("Game over")
                    quit()
        elif shop1=="Nothing":
            print("You bought nothing")
    if monster1=="yes":
        print("The monster has got to you.")
        time.sleep(2)
        print ("You fight")
        if sword=="wooden sword":
            print("You took 5 of damage during the fight")
            health=health-5
            print("Now you have {} of health".format(health))
            if health <=0:
                print ("Game over")
                quit ()
        elif sword=="fists":
            print("You lost 7 of health")
            health = health-7
            print("Now you have {} of health")
            if health <=0:
                 print ("Game over")
                 quit()




else:
    quit()

