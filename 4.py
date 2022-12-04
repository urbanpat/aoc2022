from pathlib import Path

sections = (Path(__file__).parent / "input").read_text().split("\n")[:-1]


def range_from_str(code: str) -> tuple[int, int]:
    # code is in form x-x
    start, stop = [int(c) for c in code.split("-")]
    return start, stop


sections_in_pairs = [[range_from_str(s) for s in sec.split(",")] for sec in sections]

pair_double_coverage = []
pair_overlap = []
for (e1_start, e1_stop), (e2_start, e2_stop) in sections_in_pairs:
    e1_ids, e2_ids = set(range(e1_start, e1_stop + 1)), set(range(e2_start, e2_stop + 1))

    if (intersection := e1_ids | e2_ids) <= e1_ids or (intersection <= e2_ids):
        pair_double_coverage.append(True)
    else:
        pair_double_coverage.append(False)

    if e1_ids & e2_ids:
        pair_overlap.append(True)
    else:
        pair_overlap.append(False)

print(f"one range is completely in the other in {sum(pair_double_coverage)} cases")
print(f"one range overlaps with the other in {sum(pair_overlap)} cases")
