import time

print("Welcome to space adventure say Yes to start")
food = 0
health = 10
start = input("")
if start == "Yes":
    print("You are going to space!!!! To the moon!!!!")
    money = 5
    print("You start your space adventure with 5 euros")
    print("first you think to buy food.")
    food1 = input("Do you want to buy food?Yes or No?")
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

else:
    quit()

