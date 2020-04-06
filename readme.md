# choose_multiple
This module lets you choose multiple elements of a given list.

List elements are numbered automatically and presented in columns if needed.

# Manual
## User
Input accepts space separated numbers in the range of the list's length.

## Developer
`chose_multiple` is for Python 3.6+ , console only.

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
`list`: A list of chosen elements from from_list

When nothing is entered (empty string), an empty list is returned.
# Change Log
## 2020/04/05
- change function to class
- separate input/output from logic
- add method `get_choices`