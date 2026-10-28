# Colour Analysis
# The final prototype

# Welcome, introduction and instructions for users
print("♡===========================================♡")
print("Welcome to your personalised Colour Analysis!")
print("♡===========================================♡")
print("Instructions:")
print("You will be shown four questions relating to your features such as your skins undertone, eye colour, hair colour and skin tone.")
print("You will need to answer with the letter that corresponds with which answer you choose and press Enter after each answer.")
print("You will then be shown your colour season (either spring, autumn, winter or summer)...")
print("with recommendations of which colours do/don't suit your features, along with what makeup and jewellery that makes you look best.")
print("Have fun and enjoy!!")
input("Press ENTER to begin.")

# Flag to keep the app running in a loop
keepRunning = True

# App loop
while keepRunning == True:

    # Questions 1-4

    # Question 1: undertone
    print("Are you warm or cool toned?")
    print("Suggestion: if you have green veins, pick warm, if you have blue/purple veins, pick cool.")
    print("(a) warm")
    print("(b) cool")
    undertone = input().lower()

    # Question 2: eye colour
    print("What colour would you describe your eyes?")
    print("(a) blue")
    print("(b) green")
    print("(c) brown")
    print("(d) hazel")
    eye_colour = input().lower()

    # Question 3: hair colour
    print("What colour would you describe your hair?")
    print("(a) blonde")
    print("(b) brown")
    print("(c) red")
    print("(d) black")
    hair_colour = input().lower()

    # Question 4: skin tone
    print("What tone would you describe your skin?")
    print("(a) fair")
    print("(b) medium")
    print("(c) olive")
    print("(d) tan")
    print("(e) dark")
    skin_tone = input().lower()

    # Scoring lightness of features
    # Each feature either adds or subtracts from the score based on how light the feature is.
    # Blue eyes are light so they add to the score, while dark eyes subtract
    # If the total is above 0, the person leans light, and below 0 is deep
    lightness = 0

# eyes: (a) blue, (b) green, (c) brown, (d) hazel
    if eye_colour == "a":      #blue
        lightness += 1
    elif eye_colour == "c":    # brown
        lightness -= 1

# hair: (a) blonde, (b) brown, (c) red, (d) black
    if hair_colour == "a" or hair_colour == "c":      # blonde and red
        lightness += 1
    elif hair_colour == "d":       # black
        lightness -= 2
    else:
        lightness -= 1     # brown

# skin tone: (a) fair, (b) medium, (c) tan, (d) dark
    if skin_tone == "a":        # fair
        lightness += 2
    elif skin_tone == "b":      # medium
        lightness += 1
    elif skin_tone == "c":      # olive
        lightness -= 1
    elif skin_tone == "d":      # tan
        lightness -= 2
    elif skin_tone == "e":      # dark
        lightness -= 3

    # Decide the season based on undertone
    if undertone == "a":         # warm
        if lightness > 0:
            season = "Spring"
        else:
            season = "Autumn"
    else:                         # cool
        if lightness > 0:
            season = "Summer"
        else:
            season = "Winter"

    # The results
    print("♡=============================♡")
    print("Your colour season is:", season)
    print("♡=============================♡")
    print("Your recommendations are loading...")

    # Print image of recommended colour palette
    from PIL import Image

    if season == "Spring":
        img = Image.open("Spring's Colour Palette.jpg")
        img.show()
    if season == "Autumn":
        img = Image.open("Autumn's Colour Palette.jpg")
        img.show()
    if season == "Winter":
        img = Image.open("Winter's Colour Palette.jpg")
        img.show()
    if season == "Summer":
        img = Image.open("Summer's Colour Palette.jpg")
        img.show()

    # Ask try again
    if input("Try again? (y/n)").lower()=="n":
        keepRunning = False

    # Goodbye message if user doesn't want to try again
    if keepRunning == False:
        print("Goodbye")