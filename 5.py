from collections import defaultdict
from pathlib import Path

inhalt = (Path(__file__).parent / "input").read_text().split("\n")[:-1]


def create_stacks(inhalt: list[str]) -> dict[int, list[str]]:
    setup_data = [line[1::4] for line in inhalt[:8]]
    stacks = defaultdict(list)
    for i in range(len(setup_data) + 1):
        for line in setup_data[::-1]:
            if line[i] != " ":
                stacks[i + 1].append(line[i])

    return stacks


def get_result(stacks: dict[int, list[str]]) -> str:
    res = ""
    for ch in stacks.values():
        res += ch[-1]
    return res


instructions = [line.split(" ") for line in inhalt[10:]]
_move, _from, _to = list(zip(*[(int(line[1]), int(line[3]), int(line[5])) for line in instructions]))

# reverse order
stacks = create_stacks(inhalt)
for m, f, t in zip(_move, _from, _to):
    while m > 0:
        stacks[t].append(stacks[f].pop())
        m -= 1
print(get_result(stacks))

# keep order
stacks2 = create_stacks(inhalt)
for m, f, t in zip(_move, _from, _to):
    stacks2[t].extend(stacks2[f][-m:])
    del stacks2[f][-m:]
print(get_result(stacks2))

