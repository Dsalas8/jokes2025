# Joke Game 
# CHECK LIST: lists, functions, abstraction, parameters, iteration, selection, sequencing

# List of categories
categories = ["robbers", "tanks", "pencils"]


# Dictionary of jokes (each value is a list of lines)
jokes = {
    "robbers": ["Knock knock...", "Calder...", "Calder police — I've been robbed!"],
    "tanks": ["Knock knock...", "Tank...", "You're welcome!"],
    "pencils": ["Knock knock...", "Broken pencil...", "Nevermind — it's pointless!"]
}

# FUNCTIONS (2+ required)

# Abstraction: a general function that can tell ANY joke category
def tell_joke(category):
    """Prints a joke line-by-line based on the category."""
    print("\nHere comes your joke!")
    for line in jokes[category]:   # iteration
        if "..." in line:
            input(line)            # user interacts with knock-knock lines
        else:
            print(line)
    print()




def get_valid_category():
    """Asks the user for a category and validates it."""
    print("\nAvailable categories:", ", ".join(categories))
    choice = input("Choose a category: ").lower()


    if choice in categories:
        return choice
    else:
        print("That's not a valid category.")
        return None




# -----------------------------
# MAIN PROGRAM (algorithm)


print("Welcome to the Joke Game!")


joke = input("Do you want to hear a joke? (yes/no) ").lower()


# SELECTION
if joke == "no":
    print("Okay, maybe next time!")


# ITERATION LOOP
while joke == "yes":
    category = get_valid_category()


    if category:
        tell_joke(category)  # function call with parameter


    joke = input("Do you want another joke or are you finished? ").lower()
    




# ENDING SEQUENCE
if joke == "finished":
    rating = int(input("Rate our game from 1–10: "))
    print("Thanks! Your satisfaction score is", rating * 10, "%")


    recommend = input("Would you recommend this game to a friend? (yes/no/maybe) ").lower()


    if recommend in ["yes", "maybe"]:
        print("Awesome, thanks for the support!")
    else:
        print("Sorry you didn’t enjoy it.")
