VOWELS = 'aeiou'


def is_nice(string: str) -> bool:
    return has_three_vowels(string) \
        and has_repeats(string) \
        and not has_special_substring(string)


def has_three_vowels(string: str) -> bool:
    vowels = 0
    for vowel in VOWELS:
        vowels += string.count(vowel)
    return vowels >= 3


def has_repeats(string: str) -> bool:
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True
    return False


def has_special_substring(string: str) -> bool:
    return 'ab' in string \
        or 'cd' in string \
        or 'pq' in string \
        or 'xy' in string


nice_strings = 0
with open('input.txt') as f:
    for string in f.read().splitlines():
        if is_nice(string):
            nice_strings += 1
print(f"Number of nice string is {nice_strings}")
