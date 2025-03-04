import hashlib

with open("input") as f:
    PUZZLE_INPUT = f.read().strip()


if __name__ == "__main__":
    index = 0
    part_one_password = ""
    part_two_password = ["_" for _ in range(8)]
    while True:
        digest = hashlib.md5(
            f"{PUZZLE_INPUT}{index}".encode("ascii")
        ).hexdigest()
        if digest.startswith("00000"):
            if len(part_one_password) < 8:
                part_one_password += digest[5]
            if (
                digest[5].isnumeric()
                and int(digest[5]) < 8
                and part_two_password[int(digest[5])] == "_"
            ):
                part_two_password[int(digest[5])] = digest[6]
                if not ("_" in part_two_password):
                    break
                print("".join(part_two_password))
        index += 1
    print(f"Part one answer is {part_one_password}")
    print(f"Part two answer is {"".join(part_two_password)}")
