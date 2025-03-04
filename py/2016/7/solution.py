import re


def parse_address(address: str) -> tuple[list[str], list[str]]:
    within_brackets = re.findall(r"\[(.*?)\]", address)
    outside_bracket = address
    for substring in within_brackets:
        outside_bracket = outside_bracket.replace(substring, "")
    outside_bracket = outside_bracket.split("[]")
    return outside_bracket, within_brackets


def check_abba(string: str) -> bool:
    return (
        (string[0] != string[1])
        and (string[1] == string[2])
        and (string[0] == string[3])
    )


def contains_abba(strings: list[str]) -> bool:
    for string in strings:
        for index in range(1, len(string) - 2):
            if check_abba(string[index - 1 : index + 3]):
                return True
    return False


def count_support_tls(addresses: list[str]) -> int:
    support_count = 0
    for address in addresses:
        outside, inside = parse_address(address)
        if contains_abba(inside):
            continue
        support_count += contains_abba(outside)
    return support_count


def find_babs(strings: list[str]) -> list[str]:
    babs: list[str] = []
    for string in strings:
        for index in range(0, len(string) - 2):
            if string[index] == string[index + 2]:
                babs.append(string[index : index + 3])
    return babs


def count_support_ssl(addresses: list[str]) -> int:
    support_count = 0
    for address in addresses:
        outside, inside = parse_address(address)
        for bab in find_babs(inside):
            aba = f"{bab[1]}{bab[0]}{bab[1]}"
            if any([aba in string for string in outside]):
                support_count += 1
                break
    return support_count


if __name__ == "__main__":
    with open("input") as f:
        addresses = [line.strip() for line in f.readlines()]
    print(f"Part one answer is {count_support_tls(addresses)}")
    print(f"Part two answer is {count_support_ssl(addresses)}")
