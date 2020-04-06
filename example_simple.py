from choose_multiple import ChooseMultiple
"""
Basic example usage of the ChooseMultiple class.

Only argument needed is a list of printable items
to instantiate ChooseMultiple.

In this example:
Choose your favourites from a list of movies.
To remind you of your favourites, your choices will be printed.
(See it in my upcoming TED Talk)
"""


movie_list = [
    "And Now for Something Completely Different",
    "Monty Python and the Holy Grail",
    "Monty Python's Life of Brian",
    "Monty Python Live at the Hollywood Bowl",
    "Monty Python's The Meaning of Life",
    "Monty Python Live (Mostly)"
]

cm = ChooseMultiple(movie_list)         # instantiate class

print("Choose your favourite movies\n") # show a header, recommended
cm.display_options()                    # show all options
my_movies = cm.get_choices()            # assign chosen options

if my_movies:                           # process chosen options
    print("\nYour exquisite taste encompasses movies such as")
    for mv in my_movies:
        print("- " + mv)
else:
    print("\nCancelled")

print("\nkeep fit and well\n")
