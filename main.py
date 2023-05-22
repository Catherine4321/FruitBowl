run = True
fruit_list = [
    ["Apple", "Red", 5],
    ["Pear", "Green", 7],
    ["Mango", "Yellow", 2],
    ["Kiwifruit", "Brown", 9],
    ["Peach", "Pink", 3]
]

def look_fruit(L):
    print("You look at the fruit bowl and you see: ")
    for i in range(0, len(L)):
        observation = "{}. {} {} {}".format(i, L[i][2], L[i][1], L[i][0])
        print(observation)
def add_fruit(L):
    get_answer = True
    get_amount = True
    look_fruit(L)
    while get_answer == True:
        ask = input("Are you adding a new fruit to the bowl? Type y or n: ").lower()
        if ask == 'y':
            adding = input("What would you like to add to the fruit bowl: ")
            colour = input("What is the colour of the fruit: ")
            how_much = int(input("How many would you like to add: "))
            L.append([adding, colour,  how_much])
            print("Thank-you for adding {} {} {} to the bowl".format(L[len(L)-1][2], L[len(L)-1][1], L[len(L)-1][0]))
            get_answer = False
        elif ask == 'n':
            get_index_number = True
            while get_index_number == True:
                adding = int(input("Type the index number of the fruit you'd like to add to: "))
                if adding <= len(L) - 1:
                    while get_amount == True:
                        try:
                            how_much = int(input("How many would you like to add: "))
                        except ValueError:
                            print("You can't add that. Try again.")
                        else:
                            get_amount = False
                            L[adding][2] = L[adding][2] + how_much
                            print("Thank-you. There are now {} {} in the bowl.".format(L[adding][2], L[adding][0]))
                            get_index_number = False
                else:
                    print("The fruit bowl feels empty as you remind it that it is not that full. Try again.")
            get_answer = False
        else:
            print("The fruit bowl stares at you with somewhat of a longing. You feel pity towards it. Please offer something to the bowl.")


def eat_fruit(L):
    look_fruit(L)
    eating = int(input("What fruit would you like to eat? Please input the fruit's index number: "))
    how_much = int(input("How many would you like to eat: "))
    output = "Yum! You eat {} {}. There are now {} {} left.".format(how_much, L[eating][0], L[eating][2] - how_much, L[eating][0])
    print(output)
    L[eating][2] = L[eating][2] - how_much

def menu():
    global run
    get_answer = True
    stars = "*"*40
    fruit = """
    You are standing in front of your fruit bowl, what do you do?
    a. add fruit to the fruit bowl
    b. observe the fruit
    c. eat fruit
    d. leave the fruit bowl alone
    """
    print(stars)
    print(fruit)
    while get_answer == True:
        answer = input("Please enter your answer here: ").lower()
        if answer == 'a':
            add_fruit(fruit_list)
            run = False
            get_answer = False
        elif answer == 'b':
            look_fruit(fruit_list)
            run = False
            get_answer = False
        elif answer == 'c':
            eat_fruit(fruit_list)
            run = False
            get_answer = False
        elif answer == 'd':
            print("You gently walk away from the delicate fruit bowl.")
            run = False
            get_answer = False
        else:
            print("NO! Don't do that! You'll disturb the fruit bowl! Try again.")

while run == True:
    menu()
    again = input("Would you like to approach the fruit bowl again? y or n ").lower()
    if again == "y":
        run = True
    elif again == "n":
        run = False
        print("You gently walk away from the delicate fruit bowl.")
    else:
        run = False
        print("You gently walk away from the delicate fruit bowl.")
