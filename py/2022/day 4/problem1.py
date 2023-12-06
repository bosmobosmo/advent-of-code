from typing import TypedDict


class Assignment(TypedDict):
    start: int
    end: int


def parse_input(input_list: list[str]) -> list[list[Assignment]]:
    assignment_list: list[list[Assignment]] = []
    for line in input_list:
        split = line.split(',')
        assignment_pair: list[Assignment] = []
        for part in split:
            job = part.split('-')
            assignment_pair.append(Assignment(
                start=int(job[0]), end=int(job[-1])))
        assignment_list.append(assignment_pair)
    return assignment_list


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        input_list = f.read().splitlines()
    job_list = parse_input(input_list)

    inclusive_pairs = 0
    for job in job_list:
        start_difference = job[0]['start'] - job[1]['start']
        end_difference = job[0]['end'] - job[1]['end']

        if start_difference * end_difference > 0:
            continue
        inclusive_pairs += 1

    print(inclusive_pairs)
