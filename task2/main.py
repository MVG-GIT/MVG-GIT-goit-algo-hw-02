from palindrome import is_palindrome_pretty

test = [
    "a",
    "radar",
    "rotator",
    "leper",
    "madam",
    "madam i'm adam",
    "palindrome",
    "too hot to hoot"
]


for string in test:
    print(is_palindrome_pretty(string))
