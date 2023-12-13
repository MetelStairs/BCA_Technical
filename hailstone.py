class HailstoneClass:
    def __init__(self):
        self.starting_number = self
        self.steps = 0
        self.sequence = []
        self.text_summary = ""

    def is_integer(self):
        """
        Function for checking if inputted value is Int
        """
        try:
            # If value can be converted or is already int then pass fine, else return type error
            int(self)
            return True
        except ValueError:
            return False

    def hailstone_sequence(self):
        """
        Function that does the hailstone mathematical compute
        """
        if not HailstoneClass.is_integer(self):
            raise ValueError("The starting number must be an integer")

        # Ensures the variable is an Int after checking
        self = int(self)

        if self <= 1:
            raise ValueError("The starting number must be greater than 1")

        # Initialize the empty variables for tracking steps
        steps = 0
        sequence = []
        # Make the starting number the first entry in the sequence
        orginal_starting_number = self
        sequence = [self]

        while self != 1:  # While the number is not 1
            if self % 2 == 0:  # If the number is even then divide by 2
                self = self // 2
            else:  # Otherwise if its an odd number then multiply by 3 and add 1
                self = 3 * self + 1

            steps = steps + 1  # Add +1 for each loop done
            sequence.append(self)  # Append each number to a list for the full sequence
            # Write a brief summary (I think this is what was wanted by Textual Summary)
        text_summary = f"The starting number of {orginal_starting_number} reaches 1 in {steps} steps"

        return sequence, steps, text_summary

    def main_hailstone_function(self):
        """
        Function prints the output and potential errors of the hailstone sequence
        """
        try:
            sequence, steps, text_summary = HailstoneClass.hailstone_sequence(self)

            print(f"Starting Number: {self}")
            print(f"Number of steps: {steps}")
            print(f"Sequence: {sequence}")
            print(text_summary)

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    starting_number = input("Please choose a starting number:")
    HailstoneClass.main_hailstone_function(starting_number)
