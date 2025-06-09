# FINAL PROJECT: Credit Card Expiry Report (Beginner Version)

# This program reads credit card data, finds expired cards,
# and writes a report of the expired or soon-to-expire cards.

def convert_date(month, year):
    # Convert month and year into one number like 202306
    return int(str(year) + str(month).zfill(2))

# Set today's expiry cutoff date (June 2025)
cutoff_date = convert_date(6, 2025)

# Lists to hold data
first_names = []
last_names = []
card_types = []
card_numbers = []
exp_months = []
exp_years = []
expiry_values = []

# STEP 1: Read data from file
try:
    with open("data.dat", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 6:
                first_names.append(parts[0])
                last_names.append(parts[1])
                card_types.append(parts[2])
                card_numbers.append(parts[3])
                month = int(parts[4])
                year = int(parts[5])
                exp_months.append(month)
                exp_years.append(year)
                expiry_values.append(convert_date(month, year))
except:
    print("Could not read file. Make sure 'data.dat' is in the same folder.")

# STEP 2: Sort data by expiry date using simple exchange sort
n = len(first_names)
for i in range(n):
    for j in range(i + 1, n):
        if expiry_values[i] > expiry_values[j]:
            # Swap all fields together
            first_names[i], first_names[j] = first_names[j], first_names[i]
            last_names[i], last_names[j] = last_names[j], last_names[i]
            card_types[i], card_types[j] = card_types[j], card_types[i]
            card_numbers[i], card_numbers[j] = card_numbers[j], card_numbers[i]
            exp_months[i], exp_months[j] = exp_months[j], exp_months[i]
            exp_years[i], exp_years[j] = exp_years[j], exp_years[i]
            expiry_values[i], expiry_values[j] = expiry_values[j], expiry_values[i]

# STEP 3: Write expired or soon-to-expire cards to output file
try:
    with open("expired_cards_report.txt", "w") as output:
        for i in range(n):
            if expiry_values[i] <= cutoff_date:
                status = "EXPIRED" if expiry_values[i] < cutoff_date else "RENEW IMMEDIATELY"
                line = first_names[i] + " " + last_names[i]
                line += ": " + card_types[i].ljust(12)
                line += " #" + card_numbers[i] + " "
                line += str(exp_years[i]) + str(exp_months[i]).zfill(2)
                line += " " + status + "\n"
                output.write(line)
    print("✅ Report created: expired_cards_report.txt")
except:
    print("Could not write to output file.")
