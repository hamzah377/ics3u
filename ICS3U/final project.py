Author: Hamzah Ishtiaq
Course: ICS3U
Last Updated: june 16, 2025
program: credit card report
discrption: Reads card data from a file, verifies validity with the Luhn check, highlights expired or near-expiry cards, sorts them by date, and displays a color-coded summary.

# ANSI escape codes to change terminal text color
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def luhn_check(card_number):
    # Checks if the card number is valid using the Luhn method
    reverse_digits = card_number[::-1]
    total = 0

    for i in range(len(reverse_digits)):
        num = int(reverse_digits[i])
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9
        total += num

    return total % 10 == 0

def merge_sort(cards):
    # Sorts cards based on their expiry date
    if len(cards) > 1:
        middle = len(cards) // 2
        left_half = cards[:middle]
        right_half = cards[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][-1] < right_half[j][-1]:
                cards[k] = left_half[i]
                i += 1
            else:
                cards[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            cards[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            cards[k] = right_half[j]
            j += 1
            k += 1

def parse_line(data):
    # Breaks a line into fields and validates it
    fields = data.strip().split(",")
    if len(fields) != 6:
        return None

    fname, lname, card_type, number, mo, yr = fields

    if not number.isdigit():
        return None

    try:
        mo = int(mo)
        yr = int(yr)
    except:
        return None

    if not (1 <= mo <= 12):
        return None

    expiry_value = yr * 100 + mo
    return [fname, lname, card_type, number, mo, yr, expiry_value]

def print_results(card_list):
    # Shows the final list of expired and nearly expired cards
    if not card_list:
        print(RED + "No expired or near-expiry cards found." + RESET)
        return

    print("{:<20} {:<12} {:<20} {:<6} {}".format("Name", "Card Type", "Number", "Expiry", "Status"))
    print("-" * 70)

    for item in card_list:
        color = RED if item[4] == "EXPIRED" else YELLOW
        line = "{:<20} {:<12} {:<20} {:<6} {}".format(item[0], item[1], item[2], item[3], item[4])
        print(color + line + RESET)

    print("\nTotal cards that need attention: {}".format(len(card_list)))


def main():
    # Loads data, checks dates, and shows the report
    path = "/workspaces/ICS3U_S2/ICS3U/Data/CARDNUMBERS.dat"
    cutoff = 202506
    alert_list = []

    try:
        with open(path, "r") as file:
            lines = file.readlines()

        for line in lines[1:]:
            result = parse_line(line)
            if result is None:
                continue

            fname, lname, ctype, num, mo, yr, expiry = result

            if expiry <= cutoff and luhn_check(num):
                note = "EXPIRED" if expiry < cutoff else "RENEW IMMEDIATELY"
                full_name = (fname + " " + lname + ":").ljust(20)
                type_label = ctype.ljust(12)
                num = "#" + num
                exp_str = str(yr) + str(mo).zfill(2)
                alert_list.append([full_name, type_label, num, exp_str, note, expiry])

        merge_sort(alert_list)
        print_results(alert_list)

    except FileNotFoundError:
        print(RED + "Input file not found." + RESET)
    except Exception as e:
        print(RED + "Problem occurred: " + str(e) + RESET)

if __name__ == "__main__":
    main()
