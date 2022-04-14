# Ask the user if they have played before
show_instructions = input("Have you played this game before?").lower()

# If they say yes, output 'program continues'
if show_instructions == "yes":
    print("Program Continues")

# If they say no, output 'display instructions'
else:
    print("Display instructions")
