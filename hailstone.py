
def is_integer(value):
    """
    Function for checking if inputted value is Int

    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def hailstone_sequence(starting_number):
    """
    Function that does the hailstone mathematic compute
    """
    if not is_integer(starting_number):
        raise ValueError("The starting number must be an integer")

    # Ensures the variable is an Int after checking
    starting_number = int(starting_number)

    if starting_number == 1:
        raise ValueError("The starting number cannot be 1")

    # Initialize the empty variables for tracking steps
    steps = 0
    sequence = []
    # Make the starting number the first entry in the sequence
    sequence = [starting_number]

    while starting_number != 1:  # While the number is not 1
        if starting_number % 2 == 0:  # If the number is even then divide by 2
            starting_number = starting_number // 2
        else:  # Otherwise if its an odd number then multiply by 3 and add 1
            starting_number = 3 * starting_number + 1

        steps = steps + 1  # Add +1 for each loop done
        sequence.append(starting_number)  # Append each number to a list for the full sequence
        text_summary = f"The starting number of {starting_number} reaches 1 in {steps} steps"

    return sequence, steps, text_summary


def main_hailstone_function(starting_number):
    """
    Function prints the output and potential errors of the hailstone sequence
    """
    try:
        sequence, steps, text_summary = hailstone_sequence(starting_number)

        print(f"Starting Number: {starting_number}")
        print(f"Number of steps: {steps}")
        print(f"Sequence: {sequence}")
        print(text_summary)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    start_number = "1"
    main_hailstone_function(start_number)
