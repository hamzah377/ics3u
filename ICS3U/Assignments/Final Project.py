"""
Author: Hamzah
Course: ICS3U
Last Updated: June 17, 2025
Program: Credit Card Expiry Checker
Description: Reads a customer database, finds credit cards expiring on or
             before June 2025, validates them with the Luhn algorithm, sorts
             the results by date (earliest → latest) using merge sort, and
             prints a report to the console.

VARIABLE DICTIONARY:
file_path (str)          : absolute path to the CSV data file
cutoff_date (int)        : threshold date (June 2025 → 202506) for reminders
names (list)             : customer names ("Surname, GivenName")
types (list)             : credit‑card types ("Visa" / "MasterCard")
numbers (list)           : card numbers as 16‑digit strings
months (list)            : expiry months as integers
years (list)             : expiry years as integers
dates (list)             : expiry dates in YYYYMM integer form
status (list)            : "EXPIRED" or "RENEW IMMEDIATELY"
line (str)               : one raw line read from the CSV file
fields (list)            : six comma‑separated values from a data line
first (str)              : given name from file
last (str)               : surname from file
cc_type (str)            : credit‑card type from file
cc_num (str)             : credit‑card number from file
mo (int)                 : expiry month
yr (int)                 : expiry year
full_name (str)          : formatted full name
exp_date (int)           : combined expiry date in YYYYMM form
i, j, k, mid (int)       : loop and index counters for merge sort
left_* / right_* (lists) : halves of arrays used during merge sort
reverse_digits (str)     : card number reversed for Luhn processing
digit (int)              : single digit during Luhn calculation
total (int)              : running total during Luhn check
"""

# ---------- CONSTANTS ----------
cutoff_date = 202506                       # June 2025 threshold
file_path = "/workspaces/ics3u/ICS3U/Data/data.dat"  # Data file location

# ---------- ARRAYS ----------
names = []      # Customer names
types = []      # Card types
numbers = []    # Card numbers
months = []     # Expiry months
years = []      # Expiry years
dates = []      # Combined dates (YYYYMM)
status = []     # Card status strings

# ---------- FILE I/O ----------
with open(file_path, "r") as src:          # Open file safely
    src.readline()                         # Skip header row
    for line in src:                       # Process each remaining line
        fields = line.strip().split(",")   # Split CSV into fields

        first = fields[0]                  # Given name
        last = fields[1]                   # Surname
        cc_type = fields[2]                # Card type
        cc_num = fields[3]                 # Card number
        mo = int(fields[4])                # Expiry month
        yr = int(fields[5])                # Expiry year

        full_name = last + ", " + first    # Format name
        exp_date = yr * 100 + mo           # Convert to YYYYMM

        if exp_date <= cutoff_date:        # Card needs attention
            names.append(full_name)
            types.append(cc_type)
            numbers.append(cc_num)
            months.append(mo)
            years.append(yr)
            dates.append(exp_date)
            if exp_date < cutoff_date:
                status.append("EXPIRED")
            else:
                status.append("RENEW IMMEDIATELY")

# ---------- LUHN ALGORITHM ----------
def luhn_check(card_number):               # Validate a card number
    total = 0
    reverse_digits = card_number[::-1]     # Reverse the digits
    for i in range(len(reverse_digits)):   # Traverse each digit
        digit = int(reverse_digits[i])     # Convert char to int
        if i % 2 == 1:                     # Double every 2nd digit
            digit = digit * 2
            if digit > 9:                  # Subtract 9 if > 9
                digit -= 9
        total += digit                     # Update running total
    return total % 10 == 0                 # True if total mod 10 = 0

# Remove invalid cards
i = 0
while i < len(numbers):                    # Loop through card list
    if not luhn_check(numbers[i]):         # If card fails Luhn
        del names[i]                       # Remove aligned data
        del types[i]
        del numbers[i]
        del months[i]
        del years[i]
        del dates[i]
        del status[i]
    else:
        i += 1                             # Only advance if kept

# ---------- MERGE SORT ----------
def merge_sort(dates, names, types, numbers, months, years, status):
    if len(dates) > 1:                     # More than one element?
        mid = len(dates) // 2              # Midpoint index

        # Split every array into two halves
        left_dates = dates[:mid]
        right_dates = dates[mid:]
        left_names = names[:mid]
        right_names = names[mid:]
        left_types = types[:mid]
        right_types = types[mid:]
        left_numbers = numbers[:mid]
        right_numbers = numbers[mid:]
        left_months = months[:mid]
        right_months = months[mid:]
        left_years = years[:mid]
        right_years = years[mid:]
        left_status = status[:mid]
        right_status = status[mid:]

        # Recursive sort on each half
        merge_sort(left_dates, left_names, left_types,
                   left_numbers, left_months, left_years, left_status)
        merge_sort(right_dates, right_names, right_types,
                   right_numbers, right_months, right_years, right_status)

        # Merge the two sorted halves
        i = j = k = 0
        while i < len(left_dates) and j < len(right_dates):
            if left_dates[i] < right_dates[j]:
                dates[k] = left_dates[i]
                names[k] = left_names[i]
                types[k] = left_types[i]
                numbers[k] = left_numbers[i]
                months[k] = left_months[i]
                years[k] = left_years[i]
                status[k] = left_status[i]
                i += 1
            else:
                dates[k] = right_dates[j]
                names[k] = right_names[j]
                types[k] = right_types[j]
                numbers[k] = right_numbers[j]
                months[k] = right_months[j]
                years[k] = right_years[j]
                status[k] = right_status[j]
                j += 1
            k += 1

        # Copy any leftover items from left half
        while i < len(left_dates):
            dates[k] = left_dates[i]
            names[k] = left_names[i]
            types[k] = left_types[i]
            numbers[k] = left_numbers[i]
            months[k] = left_months[i]
            years[k] = left_years[i]
            status[k] = left_status[i]
            i += 1
            k += 1

        # Copy any leftover items from right half
        while j < len(right_dates):
            dates[k] = right_dates[j]
            names[k] = right_names[j]
            types[k] = right_types[j]
            numbers[k] = right_numbers[j]
            months[k] = right_months[j]
            years[k] = right_years[j]
            status[k] = right_status[j]
            j += 1
            k += 1

# Sort all aligned arrays
merge_sort(dates, names, types, numbers, months, years, status)

# ---------- REPORT TO CONSOLE ----------
for i in range(len(dates)):                # Print each record
    line = names[i] + ":    "              # Start with name
    line += types[i] + "   "               # Add card type
    line += "#" + numbers[i] + " "         # Add card number
    if months[i] < 10:                     # Format date with 0‑padding
        line += str(years[i]) + "0" + str(months[i]) + " "
    else:
        line += str(years[i]) + str(months[i]) + " "
    line += status[i]                      # Add status
    print(line)                            # Output to console
