import random

item_collection = []

game_on = True

while game_on:
    user_input = input('Enter an item (or type "STOP" to end): ').strip().upper()

    if user_input == "STOP":
        game_on = False
    elif user_input == "":
        print("Please enter a valid item.")
    else:
        if len(item_collection) < 5:
            item_collection.append(user_input)
            print("Current collection:", item_collection)
        if len(item_collection) == 5:
            chosen_item = random.choice(item_collection)
            print(f'Your random item is: {chosen_item}')
            game_on = False  # Stop the game once a random item has been chosen

print(item_collection)
