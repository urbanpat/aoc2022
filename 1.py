from pathlib import Path

import numpy as np

path = Path(__file__).parent / "input"

food_per_elf = path.read_text().split("\n\n")

total_per_elf_calories = []
for food in food_per_elf:
    findings = food.split("\n")
    if findings[-1] == "":
        findings = findings[:-1]
    calories = [int(f) for f in findings]
    total_per_elf_calories.append(sum(calories))

total_per_elf_calories = np.array(total_per_elf_calories)

print(total_per_elf_calories.max())

order = np.argsort(-total_per_elf_calories)
best_elves = total_per_elf_calories[order]

print(best_elves[:3].sum())
