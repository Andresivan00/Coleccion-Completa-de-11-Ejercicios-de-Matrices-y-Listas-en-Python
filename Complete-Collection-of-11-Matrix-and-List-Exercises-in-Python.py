import random

# =========================
# Utilities and validations
# =========================
# In this section we define general-purpose functions that are reused
# in several exercises. Separating utilities makes code easier to test and maintain.

def ask_integer(message, minimum=None, maximum=None):
    """
    Asks the user for an integer with type and range validation.

    Parameters:
    - message: text shown to the user to request the number.
    - minimum: if specified, the entered value must be >= minimum.
    - maximum: if specified, the entered value must be <= maximum.

    Flow:
    - Repeats until the user enters a valid integer.
    - Handles ValueError if the user enters letters or non-integer numbers.
    - Checks range if minimum/maximum are provided.
    - Returns the validated integer.
    """
    while True:
        try:
            # Try to convert input to integer
            value = int(input(message))
            # Lower bound validation (if provided)
            if minimum is not None and value < minimum:
                print(f"The value must be >= {minimum}.")
                continue  # Ask again
            # Upper bound validation (if provided)
            if maximum is not None and value > maximum:
                print(f"The value must be <= {maximum}.")
                continue  # Ask again
            return value  # Valid value: return it
        except ValueError:
            # If conversion to integer fails, show message and repeat
            print("Invalid input. You must enter a whole number.")


def print_matrix(matrix, width=4):
    """
    Prints a matrix (list of lists) with aligned columns.

    Parameters:
    - matrix: list of lists (each sublist is a row).
    - width: minimum width for each element (useful for aligning numbers).
    """
    # Iterate through each row and build a string with aligned elements
    for row in matrix:
        # f"{elem:>{width}}" -> right-justified with fixed width
        print(" ".join(f"{elem:>{width}}" for elem in row))
    print()  # Blank line after matrix for clarity


def create_matrix(rows, columns, value=0):
    """
    Creates and initializes a matrix (list of lists) with a default value.

    - Avoids sharing the same internal list using nested comprehension.
    - Returns a matrix with 'rows' rows and 'columns' columns initialized to 'value'.
    """
    return [[value for _ in range(columns)] for _ in range(rows)]


# =========================
# Exercise 1
# =========================

def exercise_1():
    """
    Creates a 3x3 matrix with numbers from 1 to 9 and prints it.
    - Maintain a counter that increments to fill the matrix.
    - Build row by row and finally print with print_matrix.
    """
    matrix = []
    counter = 1  # First number to insert
    for _ in range(3):          # Repeat 3 times for the 3 rows
        row = []
        for _ in range(3):      # Repeat 3 times for the 3 columns
            row.append(counter)  # Insert counter into the row
            counter += 1         # Increment the counter
        matrix.append(row)     # Add the complete row to the matrix

    print("3x3 matrix with numbers from 1 to 9:")
    print_matrix(matrix)       # Show the matrix in readable format


# =========================
# Exercise 2
# =========================

def exercise_2():
    """
    Creates a matrix with 5 rows and n columns (n entered by user).
    - Fills with random numbers between 0 and 10 inclusive.
    - Uses list comprehension to create the matrix compactly.
    """
    n = ask_integer("Number of columns (n): ", minimum=1)  # Validate n>=1
    # Creation: for each of the 5 rows generate n random numbers
    matrix = [[random.randint(0, 10) for _ in range(n)] for _ in range(5)]

    print("5 x n matrix with random numbers between 0 and 10:")
    print_matrix(matrix)


# =========================
# Exercise 3
# =========================

def exercise_3():
    """
    Creates two square matrices A and B of size n x n (n entered by user),
    with random values, and calculates their element-wise sum in C.

    - A and B are matrices with numbers [0..9].
    - C[i][j] = A[i][j] + B[i][j].
    - Prints A, B, and C.
    """
    n = ask_integer("Size n for n x n matrices: ", minimum=1)
    # Generate A and B with nested comprehensions
    A = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    B = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    # Build C by summing element-wise
    C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

    print("Matrix A:")
    print_matrix(A)
    print("Matrix B:")
    print_matrix(B)
    print("Sum C = A + B:")
    print_matrix(C)


# =========================
# Exercise 4
# =========================
# Here we define helper functions for operations on square matrices.

def sum_row(matrix, idx):
    """Returns the sum of elements in the row with index idx."""
    return sum(matrix[idx])  # sum() adds all elements of the row list

def sum_column(matrix, idx):
    """Returns the sum of elements in the column idx."""
    # Iterate through each row and extract the element at column idx
    return sum(row[idx] for row in matrix)

def sum_main_diagonal(matrix):
    """Sums the main diagonal (positions [0,0], [1,1], ...)."""
    return sum(matrix[i][i] for i in range(len(matrix)))

def sum_secondary_diagonal(matrix):
    """Sums the secondary diagonal (positions [0,n-1], [1,n-2], ...)."""
    n = len(matrix)
    return sum(matrix[i][n - 1 - i] for i in range(n))

def matrix_average(matrix):
    """
    Calculates the arithmetic mean of all values in the matrix.
    - total: sum of all elements
    - elements: total number of cells (rows * columns)
    """
    total = sum(sum(row) for row in matrix)
    elements = len(matrix) * len(matrix[0])
    return total / elements if elements > 0 else 0


def exercise_4():
    """
    Implements a menu to operate on a 4x4 matrix.
    Important restriction:
      - Operations (2..6) cannot be executed until the matrix
        has been filled by option 1.
    - Option 1 fills the matrix with random values and sets 'filled=True'.
    - The menu loop repeats until the user chooses to exit (0).
    """
    n = 4
    matrix = create_matrix(n, n, 0)  # Initialize matrix with zeros to have structure
    filled = False  # Flag indicating if the matrix has been filled

    while True:
        print("Menu (4x4 matrix):")
        print("1. Fill ENTIRE matrix with random numbers")
        print("2. Sum a row")
        print("3. Sum a column")
        print("4. Sum main diagonal")
        print("5. Sum secondary diagonal")
        print("6. Average of all values")
        print("0. Exit")
        option = ask_integer("Choose an option: ", minimum=0, maximum=6)

        if option == 0:
            break  # Exit the menu loop and the function

        if option == 1:
            # Fill the matrix with random values between 0 and 20
            matrix = [[random.randint(0, 20) for _ in range(n)] for _ in range(n)]
            filled = True
            print("Matrix filled:")
            print_matrix(matrix)
            continue  # Return to start of loop to show menu

        # If matrix hasn't been filled yet, options 2..6 shouldn't execute
        if not filled:
            print("You must fill the matrix first (option 1).")
            continue

        # From here, filled == True, we can execute operations
        if option == 2:
            idx = ask_integer(f"Row index [0..{n-1}]: ", minimum=0, maximum=n-1)
            print(f"Sum of row {idx}: {sum_row(matrix, idx)}")
        elif option == 3:
            idx = ask_integer(f"Column index [0..{n-1}]: ", minimum=0, maximum=n-1)
            print(f"Sum of column {idx}: {sum_column(matrix, idx)}")
        elif option == 4:
            print(f"Main diagonal sum: {sum_main_diagonal(matrix)}")
        elif option == 5:
            print(f"Secondary diagonal sum: {sum_secondary_diagonal(matrix)}")
        elif option == 6:
            print(f"Matrix average: {matrix_average(matrix):.3f}")


# =========================
# Exercise 5
# =========================

def exercise_5():
    """
    Generates a 3x3 matrix with non-repeating random numbers.
    Instead of trying to generate unique numbers randomly (which can be
    inefficient), we build the list [1..9], shuffle it, and place it row by row.
    """
    numbers = list(range(1, 10))  # List with numbers 1 to 9
    random.shuffle(numbers)       # Shuffle the list in place
    # Distribute the list into 3 sublists (3 elements each)
    matrix = [numbers[i*3:(i+1)*3] for i in range(3)]

    print("3x3 matrix without repeats:")
    print_matrix(matrix)


# =========================
# Exercise 6
# =========================

def exercise_6():
    """
    Generates a matrix of size rows x columns with random numbers.
    Then RANDOMLY chooses whether to sum a row or a column, and which index to use.
    - Choosing row or column is done with random.choice([True, False]).
    - Shows the result and which random choice was made.
    """
    rows = ask_integer("Number of rows: ", minimum=1)
    columns = ask_integer("Number of columns: ", minimum=1)
    matrix = [[random.randint(0, 9) for _ in range(columns)] for _ in range(rows)]
    print("Generated matrix:")
    print_matrix(matrix)

    # Random decision: True -> row, False -> column
    choose_row = random.choice([True, False])
    if choose_row:
        # Choose a random row index within valid range
        idx = random.randint(0, rows - 1)
        total = sum_row(matrix, idx)
        print(f"RANDOMLY chose ROW {idx}. Sum = {total}")
    else:
        # Choose a random column index within valid range
        idx = random.randint(0, columns - 1)
        total = sum_column(matrix, idx)
        print(f"RANDOMLY chose COLUMN {idx}. Sum = {total}")


# =========================
# Exercise 7 (Tic-tac-toe)
# =========================

def has_winner(board, mark):
    """
    Checks if the player with 'mark' (e.g., 'X' or 'O') has won.
    - Checks all rows: if any entire row contains the mark, there's a winner.
    - Checks all columns: same logic as rows.
    - Checks both diagonals.
    Returns True if there's a victory, False otherwise.
    """
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):  # row i complete
            return True
        if all(board[j][i] == mark for j in range(3)):  # column i complete
            return True
    # Main diagonal
    if all(board[i][i] == mark for i in range(3)):
        return True
    # Secondary diagonal
    if all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def board_full(board):
    """
    Returns True if there are no empty positions ('-') on the board.
    - Uses a comprehension that traverses all rows and all characters.
    """
    return all(c != '-' for row in board for c in row)

def print_board(board):
    """Simple and clear printing of the 3x3 board for the game."""
    for row in board:
        print(" ".join(row))
    print()

def exercise_7():
    """
    Tic-tac-toe game for two human players:
    - initial board with '-' indicating empty cell.
    - current_player alternates between 'X' and 'O'.
    - Validates that the chosen position is within range and is empty.
    - After placing the mark, checks if there's a winner or if the board is full.
    """
    board = [['-' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print(f"Player {current_player}'s turn:")
        print_board(board)

        # Ask for validated row and column (0..2)
        row = ask_integer("Row [0..2]: ", minimum=0, maximum=2)
        col = ask_integer("Column [0..2]: ", minimum=0, maximum=2)

        # Check if the cell is free
        if board[row][col] != '-':
            print("Position occupied. Choose another.")
            continue  # Ask for another position

        # Place the mark
        board[row][col] = current_player

        # Check game state: victory or tie
        if has_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("Tie: no more positions.")
            break

        # Alternate player
        current_player = 'O' if current_player == 'X' else 'X'


# =========================
# Exercise 8 (Survey)
# =========================

def exercise_8():
    """
    Simulates a survey of 10 people with fields:
      - gender: 1=male, 2=female
      - works: 1=yes, 2=no
      - salary: if works, number between 600 and 2000; if not, 0
    Calculates percentages and average salaries by group.
    - Data is randomly generated to simplify the demonstration.
    """
    n = 10
    survey = []
    for _ in range(n):
        gender = random.randint(1, 2)
        works = random.randint(1, 2)
        salary = random.randint(600, 2000) if works == 1 else 0
        survey.append((gender, works, salary))

    # Calculations of totals and averages
    males = sum(1 for g, _, _ in survey if g == 1)
    females = n - males
    males_working = sum(1 for g, w, _ in survey if g == 1 and w == 1)
    females_working = sum(1 for g, w, _ in survey if g == 2 and w == 1)

    male_salaries = [salary for g, w, salary in survey if g == 1 and w == 1]
    female_salaries = [salary for g, w, salary in survey if g == 2 and w == 1]

    pct_males = 100 * males / n
    pct_females = 100 * females / n
    pct_males_working = 100 * males_working / n
    pct_females_working = 100 * females_working / n

    avg_males = sum(male_salaries) / len(male_salaries) if male_salaries else 0
    avg_females = sum(female_salaries) / len(female_salaries) if female_salaries else 0

    # Output results with readable format
    print("Generated data (gender, works, salary):")
    print(survey)
    print(f"Percentage of males: {pct_males:.1f}%")
    print(f"Percentage of females: {pct_females:.1f}%")
    print(f"Percentage of males who work: {pct_males_working:.1f}%")
    print(f"Percentage of females who work: {pct_females_working:.1f}%")
    print(f"Average salary of males who work: {avg_males:.2f}")
    print(f"Average salary of females who work: {avg_females:.2f}")


# =========================
# Exercise 9
# =========================

def selection_sort(lst):
    """
    Selection sort algorithm on a list in place.
    - Didactic purpose: explain how an O(n^2) algorithm works.
    - Not the most efficient method for large lists (use .sort() or sorted()).
    """
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        # Find the minimum in the unsorted part
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        # If we found a minimum different from i, swap
        if min_idx != i:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]


def exercise_9():
    """
    Creates a 5x5 matrix with random numbers (0..99) and performs:
      - Average of all elements.
      - Determine the maximum and how many times it appears.
      - Show all even numbers.
      - Sum main diagonal.
      - Sum the last row.
      - Sort all elements and reconstruct a sorted matrix.
    """
    n = 5
    matrix = [[random.randint(0, 99) for _ in range(n)] for _ in range(n)]
    print("Original 5x5 matrix:")
    print_matrix(matrix)

    # Calculate average
    total = sum(sum(row) for row in matrix)
    average = total / (n * n)
    print(f"Matrix average: {average:.3f}")

    # Find maximum and number of repetitions
    flat = [elem for row in matrix for elem in row]  # convert to flat list
    maximum = max(flat)
    repetitions = sum(1 for x in flat if x == maximum)
    print(f"Maximum number: {maximum}, appears {repetitions} times")

    # Extract even numbers from the flat list
    even_numbers = [x for x in flat if x % 2 == 0]
    print(f"Even numbers ({len(even_numbers)}): {even_numbers}")

    # Sum main diagonal
    main_diag = sum_main_diagonal(matrix)
    print(f"Main diagonal sum: {main_diag}")

    # Sum of last row (index -1)
    last_row_sum = sum(matrix[-1])
    print(f"Sum of last row: {last_row_sum}")

    # Sorting: sort the flat list and distribute by rows
    selection_sort(flat)
    sorted_matrix = [flat[i*n:(i+1)*n] for i in range(n)]
    print("Matrix sorted in ascending order:")
    print_matrix(sorted_matrix)


# =========================
# Exercise 10
# =========================

def exercise_10():
    """
    Reads a 5x4 matrix (20 integers) from keyboard, prints it, and shows:
      - Maximum and its positions.
      - Minimum and its positions.
    - Uses ask_integer to validate each input.
    """
    rows, columns = 5, 4
    matrix = []
    print(f"Enter {rows * columns} integers for a {rows}x{columns} matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            value = ask_integer(f"Element [{i},{j}]: ")
            row.append(value)
        matrix.append(row)

    print("Read matrix:")
    print_matrix(matrix)

    flat = [elem for row in matrix for elem in row]
    maximum = max(flat)
    minimum = min(flat)
    # Find all positions where max/min appear
    max_positions = [(i, j) for i in range(rows) for j in range(columns) if matrix[i][j] == maximum]
    min_positions = [(i, j) for i in range(rows) for j in range(columns) if matrix[i][j] == minimum]

    print(f"Maximum: {maximum}, positions: {max_positions}")
    print(f"Minimum: {minimum}, positions: {min_positions}")


# =========================
# Exercise 11
# =========================

def exercise_11():
    """
    Creates an irregular matrix (rows with different number of columns).
    - User specifies how many rows (>=2).
    - For each row, user specifies how many columns (>=1).
    - Each cell is filled with a random integer between 1 and 5.
    - Prints the matrix and the length of each row to clarify the irregularity.
    """
    rows = ask_integer("Number of rows (>=2): ", minimum=2)
    matrix = []
    for i in range(rows):
        cols = ask_integer(f"Number of columns in row {i} (>=1): ", minimum=1)
        row = [random.randint(1, 5) for _ in range(cols)]
        matrix.append(row)

    print("Generated irregular matrix:")
    for i, row in enumerate(matrix):
        print(f"Row {i} ({len(row)} col): {row}")


# =========================
# Main menu
# =========================

def main_menu():
    while True:
        print("\n======= MATRIX EXERCISES MENU =======")
        print("1. Exercise 1: 3x3 matrix with numbers 1 to 9")
        print("2. Exercise 2: 5xn matrix with random numbers")
        print("3. Exercise 3: Sum of two n x n matrices")
        print("4. Exercise 4: Menu of operations on 4x4 matrix")
        print("5. Exercise 5: 3x3 matrix without repeated numbers")
        print("6. Exercise 6: Random row or column sum")
        print("7. Exercise 7: Tic-tac-toe game")
        print("8. Exercise 8: Survey of 10 people")
        print("9. Exercise 9: Various operations on 5x5 matrix")
        print("10. Exercise 10: Read 5x4 matrix from keyboard")
        print("11. Exercise 11: Irregular matrix generation")
        print("0. Exit")
        print("======================================")

        option = ask_integer("Choose an exercise (0-11): ", minimum=0, maximum=11)

        if option == 0:
            print("Exiting program... Goodbye!")
            break
        elif option == 1: exercise_1()
        elif option == 2: exercise_2()
        elif option == 3: exercise_3()
        elif option == 4: exercise_4()
        elif option == 5: exercise_5()
        elif option == 6: exercise_6()
        elif option == 7: exercise_7()
        elif option == 8: exercise_8()
        elif option == 9: exercise_9()
        elif option == 10: exercise_10()
        elif option == 11: exercise_11()


# =========================
# Entry point
# =========================
if __name__ == "__main__":
    main_menu()
