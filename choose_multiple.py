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

    Number of columns can be determined automatically
    by providing parameter columns=0.
    Less than 20% of the options will be truncated then.

    Methods:
        __init__()
        display_options()
        get_choices()
        info()
        recommended_columns()
    """

    def __init__(self,
                 from_list,
                 columns=1,
                 line_length=79,
                 digits=2):
        """
        columns=0 applies a recommended nuber of columns.
        Less than 20% of the option texts will be truncated then.

        digits reserves space to display numbering.
        digits=2 implies a max numbering of 99.

        Parameters:
            from_list (list):  A list to chose from     mandatory
            columns (int):     Number of columns        optional, default 1
            line_length (int): avail. horizontal space  optional, default 79
            digits (int):      max length of numbers    optional, default 2
        """
        self.from_list = from_list

        self.option = {
            num: opt for num, opt in enumerate(from_list, start=1)
        }

        self.line_length = line_length
        self.digits = digits
        self.num_length = self.digits + 3  # space for numbers, "|" and ": "
        self.columns = columns if columns else self.recommend_columns()
        self.opt_length = (self.line_length - self.num_length*self.columns) // self.columns
        # max available space to display one option
        self.rows = len(from_list) // self.columns + 1  # always round up

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

    def info(self):
        """Display derived information."""
        def avg_length_longest():
            num_longest = total_elem // 5 * 4  # 80% of elements
            sort_long_20 = lens[num_longest:]
            return sum(sort_long_20) // len(sort_long_20)

        def too_long():
            tl = len([lo for lo in vals if len(lo) > self.opt_length])
            tlp = int(tl / total_elem * 100)
            return tl, tlp

        total_elem = len(self.option)
        vals = [val for val in self.option.values()]
        lens = sorted([len(opt) for opt in vals])
        rec_cols = self.recommend_columns()

        print("Columns:", self.columns)
        print("Rows:   ", self.rows)
        print("  Width of a column:", self.line_length // self.columns)
        print("  Space for option: ", self.opt_length)
        print("  Recommended:      ", rec_cols, "columns with", len(self.option)//rec_cols+1, "rows")

        print("Number of options:", total_elem)
        print("  Options too long: {} ({}%)".format(*too_long()))
        print("  Length of longest: {}".format(max(lens)))
        print("  Avg. length of longest 20%:", avg_length_longest())

    def recommend_columns(self):
        """
        Return number of columns so that only 20% of the option texts would be truncated.
        :return:
        """
        def percentage():
            space_avail = (self.line_length - c*self.num_length) // c
            num_trunced = len([val for val in self.option.values() if len(val) > space_avail])
            pct = num_trunced / len(self.option)
            return pct

        c = 1
        while percentage() < 0.2:
            c += 1
        return c-1 if c else 1
