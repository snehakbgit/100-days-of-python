print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# if else conditional operator
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45<=age<=55:
        bill= 0
        print("Middle-aged tickets are $0.")
    else:
        bill = 12
        print("Adult tickets are $12.")    
    

    wants_photo = input("Do you want to have a photo take? y for yes and n for no: ")
    if wants_photo == "y":
        # add $3 to bill for photo
        bill = bill + 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you ride.")