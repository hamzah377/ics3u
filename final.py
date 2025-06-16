"""
Author: Hamzah Ishtiaq
Course: ICS3U
Last Updated: june 16, 2025
Program : Credit Card Report
Description : Report of all credit cards in the customer database that have expired or are about to expire.
"""

def merge_sort(expiry_list, names_list, numbers_list, brands_list, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(expiry_list, names_list, numbers_list, brands_list, left, mid)
        merge_sort(expiry_list, names_list, numbers_list, brands_list, mid + 1, right)
        merge(expiry_list, names_list, numbers_list, brands_list, left, mid, right)

def merge(expiry_list, names_list, numbers_list, brands_list, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_exp = [0] * n1
    left_names = [0] * n1
    left_nums = [0] * n1
    left_brands = [0] * n1

    right_exp = [0] * n2
    right_names = [0] * n2
    right_nums = [0] * n2
    right_brands = [0] * n2

    for i in range(n1):
        left_exp[i] = expiry_list[left + i]
        left_names[i] = names_list[left + i]
        left_nums[i] = numbers_list[left + i]
        left_brands[i] = brands_list[left + i]

    for j in range(n2):
        right_exp[j] = expiry_list[mid + 1 + j]
        right_names[j] = names_list[mid + 1 + j]
        right_nums[j] = numbers_list[mid + 1 + j]
        right_brands[j] = brands_list[mid + 1 + j]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if left_exp[i] <= right_exp[j]:
            expiry_list[k] = left_exp[i]
            names_list[k] = left_names[i]
            numbers_list[k] = left_nums[i]
            brands_list[k] = left_brands[i]
            i += 1
        else:
            expiry_list[k] = right_exp[j]
            names_list[k] = right_names[j]
            numbers_list[k] = right_nums[j]
            brands_list[k] = right_brands[j]
            j += 1
        k += 1

    while i < n1:
        expiry_list[k] = left_exp[i]
        names_list[k] = left_names[i]
        numbers_list[k] = left_nums[i]
        brands_list[k] = left_brands[i]
        i += 1
        k += 1

    while j < n2:
        expiry_list[k] = right_exp[j]
        names_list[k] = right_names[j]
        numbers_list[k] = right_nums[j]
        brands_list[k] = right_brands[j]
        j += 1
        k += 1

# Input file name
input_filename = "data (2).dat"

# Open and read file contents
with open(input_filename, 'r') as infile:
    raw_lines = infile.readlines()

# Remove header line
header = raw_lines.pop(0)

# Lists to hold parsed data
full_names = []
cc_numbers = []
cc_brands = []
expiry_codes = []

for line in raw_lines:
    first, last, brand, number, exp_mo, exp_yr = line.strip().split(',')

    full_name = first + ' ' + last
    full_names.append(full_name)
    cc_brands.append(brand)
    cc_numbers.append(number)

    # Pad month if single digit
    if len(exp_mo) == 1:
        exp_mo = '0' + exp_mo

    expiry_code_str = exp_yr + exp_mo
    expiry_codes.append(int(expiry_code_str))

# Sort all lists by expiry_codes
merge_sort(expiry_codes, full_names, cc_numbers, cc_brands, 0, len(expiry_codes) - 1)

# Process and print report lines
for idx in range(len(expiry_codes)):
    if expiry_codes[idx] < 202505:
        status = "EXPIRED"
    elif expiry_codes[idx] == 202505 or expiry_codes[idx] == 202506:
        status = "RENEW IMMEDIATELY"
    else:
        continue  # skip cards expiring later than June 2025

    print("%-35s %-15s %-20s %-10s %-15s" % (
        full_names[idx] + ':', cc_brands[idx], '#' + cc_numbers[idx], expiry_codes[idx], status))
