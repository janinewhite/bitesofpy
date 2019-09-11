VALID_COLORS = ['blue', 'yellow', 'red']

def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    chose_quit = False
    while not chose_quit:
        color = str(input("Enter a color.")).lower()
        chose_quit = (color=="quit")
        if color in VALID_COLORS:
            print(color)
        elif not chose_quit:
            print("Not a valid color")
        else:
           print("bye")
           break
    pass