SAMPLES = [
    "aaaaa-bbb-z-y-x-123[abxyz]",
    "a-b-c-d-e-f-g-h-987[abcde]",
    "not-a-real-room-404[oarel]",
    "totally-real-room-200[decoy]",
]


def detect_room(room: str) -> int:
    name = "".join(room.split("-")[:-1])
    checksum = room.split("-")[-1].split("[")[-1].strip("]")
    letters_count: dict[str, int] = {}
    for letter in sorted(name):
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1
    sorted_name = sorted(
        letters_count.items(), key=lambda x: x[1], reverse=True
    )[0:5]
    if checksum == "".join([x[0] for x in sorted_name]):
        return int(room.split("-")[-1].split("[")[0])
    return 0


def rotate_room(room: str) -> str:
    room_id = int(room.split("-")[-1].split("[")[0])
    key = room_id % 26
    new_room = ""
    for letter in room:
        if letter.isnumeric():
            break
        if letter == "-":
            new_room += letter
            continue
        new_letter_ord = ord(letter) + key
        if new_letter_ord > ord("z"):
            new_letter_ord -= 26
        new_room += chr(new_letter_ord)
    new_room += f"{room.split("-")[-1]}"
    return new_room


if __name__ == "__main__":
    for sample in SAMPLES:
        print(detect_room(sample))
    part_one_sum = 0
    real_rooms: list[str] = []
    with open("input") as f:
        for line in f.readlines():
            room_number = detect_room(line.strip())
            if room_number:
                part_one_sum += room_number
                real_rooms.append(rotate_room(line.strip()))
        print(f"Part one answer is {part_one_sum}")
        with open("room_names", "w") as f:
            for room in real_rooms:
                f.write(room + "\n")
