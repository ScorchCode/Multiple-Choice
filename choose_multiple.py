"""
Choose multiple elements from a list.

For user interaction, console only.

A given list is automatically numbered and printed.
Output in columns if needed.

Elements are chosen by entering a
space separated sequence of numbers.
"""


class ChooseMultiple:
    """
    Choose multiple elements from a list.

    List elements must be printable.
    Entry accepts space separated numbers,
    may be empty.

    When there is a large number of options to be shown,
    output can be arranged in columns.
    Depending on the horizontal space, long option texts
    are truncated (for display only).

    Methods:
        __init__()
        display_options()
        get_choices()
    """

    def __init__(self,
                 from_list,
                 columns=1,
                 line_length=79,
                 digits=2):
        """
        Parameters:
            from_list (list):  A list to chose from     mandatory
            columns (int):     Number of columns        optional, default 1
            line_length (int): avail. horizontal space  optional, default 79
            digits (int):      max length of numbers    optional, default 2
        """
        self.from_list = from_list
        self.columns = columns

        self.option = {
            num:opt for num, opt in enumerate(from_list, start=1)
        }

        self.line_length = line_length
        self.digits = digits
        self.num_length = self.digits + 3  # space for numbers, "|" and ": "
        self.opt_length = (self.line_length - self.num_length*columns) // columns
        # max available space to display one option
        self.rows = len(from_list) // columns + 1  # always round up

    def display_options(self):
        """
        Display options to chose from.
        """
        if self.columns == 1:
            out = " {:" + str(self.digits) + "}: {}"
            # simplify for single column
        else:
            out = "|{:" + str(self.digits) + "}: {:" + str(self.opt_length) + "}"
        for r in range(self.rows):
            for c in range(self.columns):
                index = r + c*self.rows + 1  # no key for index 0
                try:
                    opt = self.option[index]
                except KeyError:  # if key too high
                    break         # terminate row early
                if len(opt) > self.opt_length:
                    opt = opt[:self.opt_length]  # truncate long text
                print(out.format(index, opt), end="")
            print()  # explicit line break at end of row

    def get_choices(self,
                    in_prompt="Enter space separated numbers: ",
                    on_bad_number="Numbers only",
                    on_bad_index="Unknown option"):
        """
        Make your choices safely.

        Enter space separated numbers.
        Repeat until input is valid.

        Parameters:
            in_prompt(str):      Prompt for expected input
            on_bad_number (str): Message to display on non-numerical input
            on_bad_index (str):  Message to display on out-of-range numbers

        Returns:
            list: A subset of from_list
        """

        while True:
            inp = input(in_prompt)
            try:
                choice = [self.option[int(opt)] for opt in inp.split()]
            except ValueError:
                print(on_bad_number)
            except KeyError:
                print(on_bad_index)
            else:
                return choice

