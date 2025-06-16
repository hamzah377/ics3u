data_lines = []   # Stores lines of data from the file
dates = []        # Numeric representations of dates
answers = []      # Corresponding Wordle words

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  # Month abbreviations

file_loaded = True  # Indicates if the file was read successfully

try:
    with open("/workspaces/ICS3U_S2/ICS3U/Data/wordle.dat", "r") as file:
        for line in file:
            data_lines.append(line.strip().split())
except OSError as error:
    print("File error:", error)
    file_loaded = False

if file_loaded:

    def convert_to_date(month, day, year):
        value = int(year) * 10000
        value += (months.index(month) + 1) * 100
        value += int(day)
        return value

    for line in data_lines:
        dates.append(convert_to_date(line[0], line[1], line[2]))
        answers.append(line[3])

    def find_date_by_word(word):
        word = word.upper()
        if word in answers:
            return dates[answers.index(word)]
        return 0

    def find_word_by_date(month, day, year):
        numeric_date = convert_to_date(month, day, year)
        if numeric_date in dates:
            return answers[dates.index(numeric_date)]
        return None

    print("Welcome to the Wordle Finder!")

    choice = input("Enter 'w' to search by word or 'd' to search by date: ").lower()

    if choice == "w":
        word_input = input("Enter a word to look up: ")
        match_date = find_date_by_word(word_input)
        if match_date > 0:
            print("The word", word_input.upper(), "was used on", match_date)
        else:
            print(word_input.upper(), "was not found.")

    elif choice == "d":
        year_input = input("Enter the year: ")
        month_input = input("Enter the month (e.g. Jan): ").capitalize()
        day_input = input("Enter the day: ")

        numeric_date = convert_to_date(month_input, day_input, year_input)

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
