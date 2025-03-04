SAMPLE = [
    "eedadn",
    "drvtee",
    "eandsr",
    "raavrd",
    "atevrs",
    "tsrnev",
    "sdttsa",
    "rasrtv",
    "nssdts",
    "ntnada",
    "svetve",
    "tesnvt",
    "vntsnd",
    "vrdear",
    "dvrsen",
    "enarar",
]


def count_per_column(messages: list[str]) -> list[dict[str, int]]:
    letter_counts: list[dict[str, int]] = [{} for _ in range(len(messages[0]))]
    for message in messages:
        for index, char in enumerate(message):
            if char in letter_counts[index]:
                letter_counts[index][char] += 1
            else:
                letter_counts[index][char] = 1
    return letter_counts


if __name__ == "__main__":
    part_one_message = ""
    part_two_message = ""
    with open("input") as f:
        messages = [line.strip() for line in f.readlines()]
    counts = count_per_column(messages)
    for count in counts:
        part_one_message += max(count.items(), key=lambda x: x[1])[0]
        part_two_message += min(count.items(), key=lambda x: x[1])[0]
    print(f"Part one answer is {part_one_message}")
    print(f"Part two answer is {part_two_message}")
