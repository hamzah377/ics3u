# Palindrome Checker Program
# This program checks if each word in a list is a palindrome (same forwards and backwards)

print("Palindrome program!")

# List of words to check (some are palindromes, some are not)
word_list = ["racecar", "noon", "desk", "civic", "store", "refer", "level", "lamp", "rotor", "school"]

# Go through each word in the list
for word in word_list:
    is_palindrome = True  # Start by assuming the word is a palindrome

    # Find the middle of the word (we don't need to check past this point)
    max_check = len(word) // 2

    # Check each letter from the start with its matching letter from the end
    for i in range(max_check):
        if word[i] != word[len(word) - 1 - i]:
            is_palindrome = False  # We found a mismatch
            i = max_check  # Exit the loop early without using 'break'

    # Print result for each word
    if is_palindrome:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

print("Goodbye!")
