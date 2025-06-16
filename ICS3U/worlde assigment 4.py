Author: Hamzah Ishtiaq
Course: ICS3U
Last Updated: june 16, 2025
Program: Wordle Finder
Description: This program lets the user search a Wordle solution file
either by entering a word or by entering a specific date.

# Wordle Finder Program
# This program reads from a data file containing Wordle answers and their corresponding dates.
# The user can look up the date a specific word was used, or find the word used on a given date.

# Lists to store file data
data_lines = []   # Will hold each line from the file as a list of values [Month, Day, Year, Word]
dates = []        # Stores converted dates in numeric format (YYYYMMDD)
answers = []      # Stores Wordle answers

# Month names for conversion from string to numeric value (index + 1)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Flag to track if file was loaded correctly
file_loaded = True

# Try to open the data file and read its contents
try:
    with open("/workspaces/ICS3U_S2/ICS3U/Data/wordle.dat", "r") as file:
        for line in file:
            # Strip newline and split line into parts: [Month, Day, Year, Word]
            data_lines.append(line.strip().split())
except OSError as error:
    # If file cannot be opened, print the error and set flag to False
    print("File error:", error)
    file_loaded = False

# Proceed only if the file was loaded successfully
if file_loaded:

    # -----------------------------------
    # Function: convert_to_date
    # Converts a month, day, and year into a numeric date: YYYYMMDD
    # Example: ("Feb", 15, 2023) -> 20230215
    # -----------------------------------
    def convert_to_date(month, day, year):
        value = int(year) * 10000                     # Start with year shifted left 4 digits
        value += (months.index(month) + 1) * 100      # Convert month to number and shift left 2 digits
        value += int(day)                             # Add day
        return value

    # Loop through each line in the file data and populate dates and answers lists
    for line in data_lines:
        dates.append(convert_to_date(line[0], line[1], line[2]))  # Convert date to numeric form
        answers.append(line[3].upper())  # Store word in uppercase for easy comparison

    # -----------------------------------
    # Function: find_date_by_word
    # Given a word, return the date it was used (numeric format)
    # -----------------------------------
    def find_date_by_word(word):
        word = word.upper()
        if word in answers:
            return dates[answers.index(word)]
        return 0  # Return 0 if word not found

    # -----------------------------------
    # Function: find_word_by_date
    # Given a month, day, and year, return the Wordle word for that date
    # -----------------------------------
    def find_word_by_date(month, day, year):
        numeric_date = convert_to_date(month, day, year)
        if numeric_date in dates:
            return answers[dates.index(numeric_date)]
        return None  # Return None if date not found

    # -----------------------------
    # User Interaction Section
    # -----------------------------
    print("Welcome to the Wordle Finder!")

    # Ask the user whether they want to search by word or by date
    choice = input("Enter 'w' to search by word or 'd' to search by date: ").lower()

    # If user chooses to look up a word
    if choice == "w":
        word_input = input("Enter a word to look up: ")
        match_date = find_date_by_word(word_input)
        if match_date > 0:
            print("The word", word_input.upper(), "was used on", match_date)
        else:
            print(word_input.upper(), "was not found.")

    # If user chooses to look up a date
    elif choice == "d":
        year_input = input("Enter the year (e.g. 2023): ")
        month_input = input("Enter the month (e.g. Jan): ").capitalize()
        day_input = input("Enter the day (e.g. 15): ")

        # Convert to numeric date
        numeric_date = convert_to_date(month_input, day_input, year_input)

        # Check if date is within the valid Wordle range
        if numeric_date < 20210619:
            print(numeric_date, "is before the first Wordle. Try something later.")
        elif numeric_date > 20240421:
            print(numeric_date, "is too recent. Our data only goes up to 20240421.")
        else:
            word_result = find_word_by_date(month_input, day_input, year_input)
            if word_result is not None:
                print("The word on", numeric_date, "was", word_result)
            else:
                print("No word found for", numeric_date)

