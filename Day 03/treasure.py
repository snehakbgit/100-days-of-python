
print('''  
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("🏝️ WELCOME TO TREASURE ISLAND 🏝️")
print("An ancient land of secrets, danger, and hidden gold...\n")

choice_1 = input(
    "🧭 Your mission: FIND THE TREASURE 💰\n"
    "You arrive at a dark crossroads.\n"
    "Do you choose the LEFT path or the RIGHT path? ➡️⬅️ : "
).lower()

if choice_1 == "left":
    choice_2 = input(
        "\n🌊 You reach a deep, silent lake.\n"
        "The water looks dangerous and cold.\n"
        "Do you want to SWIM across or WAIT patiently? 🏊‍♂️⏳ : "
    ).lower()

    if choice_2 == "wait":
        choice_3 = input(
            "\n🚪 A boat takes you to an ancient temple.\n"
            "Inside are three mysterious doors glowing faintly.\n"
            "Which door will you open? RED 🔴, BLUE 🔵, or YELLOW 🟡 : "
        ).lower()

        if choice_3 == "red":
            print("\n🔥 The door erupts in flames! You are burned alive.\n💀 GAME OVER 💀")
        elif choice_3 == "blue":
            print("\n🐺 Savage beasts leap out from the darkness!\n💀 GAME OVER 💀")
        elif choice_3 == "yellow":
            print("\n🏆 The room fills with golden light!\n💰 CONGRATULATIONS! YOU FOUND THE TREASURE! 💰")
        else:
            print("\n⚠️ You hesitate too long...\n💀 GAME OVER 💀")    
    else:
        print("\n🐟 A giant trout attacks and drags you underwater!\n💀 GAME OVER 💀")    
else:
    print("\n🕳️ The ground collapses beneath you...\n💀 GAME OVER 💀")


