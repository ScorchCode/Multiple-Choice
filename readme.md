# choose_multiple
This module lets you choose multiple elements of a given list.

# Manual
## User
Input accepts space separated numbers in the range of the list's length.

## Developer
`chose_multiple` is for console only.

### Parameters:
- `from_list (list)`: A list to chose from. 
Items of the `from_list` must be printable.
`str` is the obvious type to use, but it works with any type that has a `__str__` method.

- `columns (int)`: Number of columns to display. The (default) single column display has a slightly simplified design.

A large number of options can be displayed as columns in order to still fit on screen without scrolling.
Long option text will be truncated though. The more columns, the more gets truncated.
See `example_columns.py` for an example.

See docstrings for more parameters.
### Returns:
`list`: A list of chosen elements from from_list

When nothing is entered (empty string), an empty list is returned.
# Change Log
## 2020/04/05
- change function to class
- separate input/output from logic
- add method `get_choices`