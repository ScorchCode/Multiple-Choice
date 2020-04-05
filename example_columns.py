from choose_multiple import ChooseMultiple
"""
Extended example usage of the ChooseMultiple class

with lots of options and # of columns set to 3.
"""


sketch = [
    "Arthur 'Two Sheds' Jackson", "The Funniest Joke in the World", "Flying Sheep", "Bicycle Repair Man", "Seduced Milkmen", "Self Defence Against Fresh Fruit", "Confuse-a-Cat", "Silly Job Interview", "Dead Parrot sketch", "Hell's Grannies", "A Man with a Tape Recorder Up His Nose", "Kilimanjaro Expedition", "The Lumberjack Song", "Bank Robber in a Lingerie Shop", "The First Man to Jump the Channel", "Upper Class Twit of the Year", "The Ministry of Silly Walks",
    "Tobacconist's", "The Spanish Inquisition", "Motor Insurance Sketch", "Gumby Frog Curse", "Blackmail", "Seven Brides for Seven Brothers", "Ken Clean-Air System", "Throat Wobbler Mangrove", "Election Night Special", "Silly doctor sketch", "Exploding Penguin on the TV Set", "Conrad Poohs and His Dancing Teeth", "Crelm Toothpaste", "How Not to Be Seen", "Dirty Hungarian Phrasebook", "World Forum – Communist Quiz", "Hospital for Over-Actors", "Gumby Flower Arranging", "Spam", "Exploding Version of 'The Blue Danube'", "Undertakers sketch",
    "Njorl's Saga", "The Fish-Slapping Dance", "Inspector Flying Fox of the Yard", "Blood, Devastation, Death, War and Horror", "Gumby Brain Specialist", "Cheese Shop sketch", "The Cycling Tour", "Dennis Moore", "No Time to Lose", "Spot the Looney", "The Dirty Vicar Sketch",
    "Buying an Ant", "Toupee Department", "Woody and Tinny Words", "Piston Engine (a Bargain)", "Mr. Neutron", "The Walking Trees of Dahomey", "Batsmen of the Kalahari"
]

cm = ChooseMultiple(sketch, columns=3)

print("\nPick your favourites\n")
cm.display_options()
my_choice = cm.get_choices(
    in_prompt="\nMake your choice: ",
    on_bad_number="Bad input, probably not a number",
    on_bad_index="Bad option, probably too high"
)

if my_choice:
    print("\nGood choice!")
    for c in my_choice:
        print("- " + c)
else:
    print("\nCancelled")

print("\nkeep fit and well\n")
