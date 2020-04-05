from choose_multiple import ChooseMultiple
"""
Basic example usage of the ChooseMultiple class.

Only argument needed is a list of printable elements
to init ChooseMultiple.
"""


movie = [
    "And Now for Something Completely Different",
    "Monty Python and the Holy Grail",
    "Monty Python's Life of Brian",
    "Monty Python Live at the Hollywood Bowl",
    "Monty Python's The Meaning of Life",
    "Monty Python Live (Mostly)"
]

# print("\nChoose your favourites from a list of movies.")
# print("To remind you of your favourites, your choices will be printed.")
# print("(See it in my upcoming TED Talk)\n\n")

cm = ChooseMultiple(movie)              # instantiate class

print("Choose your favourite movies\n")   # show a header, recommended
cm.display_options()                    # show all options
my_genre = cm.get_choices()             # assign chosen options

if my_genre:                            # process chosen options
    print("\nYour exquisite taste encompasses movies such as")
    for gnr in my_genre:
        print("- " + gnr)
else:
    print("\nCancelled")

print("\nkeep fit and well\n")
