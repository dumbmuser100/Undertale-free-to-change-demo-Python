Playerhp = 20
x = int(input("whats your input"))
z = x
lives = 1
attack = 10
spare = 5
if z == 1:
    animal = "Froggit"
elif z == 2:
    animal = "Froggit"
elif z == 3:
    animal = "Whimsum"
elif z == 4:
    animal = "Froggit"
elif z == 5:
    animal = "Froggit"
elif z == 6:
    animal = "Whimsum"
elif z == 7:
    animal = "Froggit"
elif z == 8:
    animal = "Froggit"
else:
    print("Sorry number not recognised you will get another animal still")
    animal = "Final Froggit"
    
text = "you encountered a " + animal
print(text)
if animal == "Final Froggit":
    health = 40
    attack = 10
    defv = 5
    print("health 40")
    print("attack 10")
    print("defense 5")
elif animal == "Froggit":
    health1 = 20
    attack1 = 5
    defv1 = 3
    print("health 20")
    print("attack 5")
    print("defense 3")
else:
    health2 = 5
    attack2 = 2
    defv2 = 0
    print("health 5")
    print("attack 2")
    print("defense 0")
m = input("What do you do")
if m == "Attack":
    if animal == "Final Froggit":
        health = health - attack + defv
        print("New HP is",+  health)
        Rev_ATk1 = attack
        Playerhp = Playerhp - Rev_ATk1
        print("oh no the Final Froggit attacked your new health is",+ Playerhp )
        m = input("What do you do now")
        if m == "Attack":
            if animal == "Final Froggit":
                health = health - attack + defv
                print("New HP is",+  health)
                Rev_ATk1 = attack
                Playerhp = Playerhp - Rev_ATk1
                print("oh no the Final Froggit attacked your new health is",+ Playerhp )
                print("you died")
