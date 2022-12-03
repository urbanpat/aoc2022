import string
from pathlib import Path

rucksacks = (Path(__file__).parent / "input").read_text().split("\n")[:-1]
common_items = [list(set(r[len(r)//2:]) & (set(r[:len(r)//2])))[0] for r in rucksacks]
print(sum([(string.ascii_lowercase + string.ascii_lowercase.upper()).index(item) + 1 for item in common_items]))

groups = list(zip(*(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])))
common_items_in_groups = [list(set(e1) & (set(e2)) & (set(e3)))[0] for e1, e2, e3 in groups]
print(sum([(string.ascii_lowercase + string.ascii_lowercase.upper()).index(item) + 1 for item in common_items_in_groups]))
