# choose_multiple
This module lets you choose multiple elements of a given list.

List elements are numbered automatically and presented in columns if needed.

# Manual
## User
Input accepts space separated numbers in the range of the list's length.

Output of `example_simple.py`:
```
Choose your favourite movies

  1: And Now for Something Completely Different
  2: Monty Python and the Holy Grail
  3: Monty Python's Life of Brian
  4: Monty Python Live at the Hollywood Bowl
  5: Monty Python's The Meaning of Life
  6: Monty Python Live (Mostly)

Enter space separated numbers: 3 5 1

Your exquisite taste encompasses movies such as
- Monty Python's Life of Brian
- Monty Python's The Meaning of Life
- And Now for Something Completely Different

``` 

## Developer
`chose_multiple` is for Python 3.6+ , console only.

Above output is created with this example code
```
from choose_multiple import ChooseMultiple

movie_list = [
    "And Now for Something Completely Different",
    "Monty Python and the Holy Grail",
    "Monty Python's Life of Brian",
    "Monty Python Live at the Hollywood Bowl",
    "Monty Python's The Meaning of Life",
    "Monty Python Live (Mostly)"
]

cm = ChooseMultiple(movie_list)

print("Choose your favourite movies\n") # show a header, recommended
cm.display_options()                    # show all options
my_movies = cm.get_choices()            # assign chosen options

if my_movies:                           # process chosen options
    print("\nYour exquisite taste encompasses movies such as")
    for mv in my_movies:
        print("- " + mv)
else:
    print("\nCancelled")
```

### Parameters:
Instantiation of `ChooseMultiple` accepts parameters, the most important of which are 

- `from_list (list)`: A list to chose from. 

- `columns (int)`: Number of columns to display.

Elements of the `from_list` must be printable.
`str` is the obvious type to use, but it works with any type that has a `__str__` method.

A large number of options can be displayed as columns in order to still fit on screen without scrolling.
Long option text will be truncated though. The more columns, the more gets truncated.
See `example_columns.py` for an example.

A tradeoff number of columns can be defined by providing parameter `columns=0`.
Less than 20% of the options will be truncated then.

See docstrings for more parameters.
### Returns:
`list`: A list of chosen elements from `from_list`

When nothing is entered (empty string), an empty list is returned.
# Change Log
## 2020/04/06
- add info() (for development only)
- add recommended number of columns
## 2020/04/05
- change function to class
- separate input/output from logic
- add method `get_choices`