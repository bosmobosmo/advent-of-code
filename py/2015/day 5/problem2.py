def is_really_nice(string: str) -> bool:
    return has_double_repeats(string) and has_repeat_with_wall(string)


def has_double_repeats(string: str) -> bool:
    for substring in get_substrings(string):
        if string.count(substring) >= 2:
            return True
    return False


def get_substrings(string: str) -> list[str]:
    substrings = []
    for i in range(len(string) - 1):
        substrings.append(string[i] + string[i+1])
    return substrings


def has_repeat_with_wall(string: str) -> bool:
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True
    return False


really_nice_string = 0
with open('input.txt') as f:
    for string in f.read().splitlines():
        if is_really_nice(string):
            really_nice_string += 1
print(f"Number of strings that are really really nice is {really_nice_string}")
