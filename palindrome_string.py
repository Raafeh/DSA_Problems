""" Q2. Given a string s, find the size of the largest palindrome that can be formed using the characters of the string. 
A palindrome is a word, phrase, number, or other sequence of characters that reads 
the same forward and backward. You can rearrange the characters in the string as needed.
Write a function largest_palindrome_size(s: str) -> int to solve the problem.
 """


def largest_palindrome_size(s: str) -> int:
    char_counts = {}  # Dictionary to store the counts of characters

    # Count the occurrences of each character in the string
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_count = 0  # Count of characters with odd occurrences

    # Iterate through the character counts
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1

    # If there are no characters with odd occurrences, the string itself is a palindrome
    if odd_count == 0:
        return len(s)
    else:
        # Otherwise, we can form a palindrome by using all characters with even occurrences,
        # plus one character with an odd occurrence as the palindrome's center.
        return len(s) - (odd_count - 1)

# Example usage:
string = "aabbccdddee"
print(largest_palindrome_size(string))  # Output: 11

    

    



