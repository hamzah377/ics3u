# name: Hamzah Ishtiaq
# student number: 1004048
# course: ICS3U
# Teacher: Mr. King
# Assignmnet: Final project - credit card report
# Date: June 17, 2025
# this program reads credit card data and checks if any cards are expired or near expiry
# it sorts them by expiry date and saves the results to a file

# CONSTANTS
EXP_MONTH = 6
EXP_YEAR = 2025
EXP_DATE_CUTOFF = EXP_YEAR * 100 + EXP_MONTH

# INPUT / OUTPUT FILES
INPUT_FILE = "data.dat"
OUTPUT_FILE = "output.txt"

# List to hold all customer data
customers = []

# Read and parse data
try:
    with open(INPUT_FILE, "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if len(fields) == 6:
                first, last, cc_type, cc_number = fields[0], fields[1], fields[2], fields[3]
                month, year = int(fields[4]), int(fields[5])
                expiry = year * 100 + month
                customers.append((expiry, first, last, cc_type, cc_number))

    # Filter and sort expired or soon-to-expire cards
    expired_customers = [entry for entry in customers if entry[0] <= EXP_DATE_CUTOFF]
    expired_customers.sort()  # sort by expiry date (YYYYMM)

    # Write to output file
    with open(OUTPUT_FILE, "w") as out:
        for expiry, first, last, cc_type, cc_number in expired_customers:
            year = expiry // 100
            month = expiry % 100
            expiry_str = f"{year}{month:02d}"
            status = "EXPIRED" if expiry < EXP_DATE_CUTOFF else "RENEW IMMEDIATELY"
            out.write(f"{first} {last}: {cc_type:<13} #{cc_number} {expiry_str} {status}\n")

    print("✅ Credit card report generated:", OUTPUT_FILE)

except FileNotFoundError:
    print(f"❌ Error: '{INPUT_FILE}' not found. Please place it in the same folder.")

except Exception as e:
    print(f"❌ Unexpected error: {e}")
