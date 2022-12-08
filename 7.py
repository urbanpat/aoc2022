from collections import defaultdict
from pathlib import Path

cd_outputs = (Path(__file__).parent / "input").read_text().split("$ cd ")[1:]
cd_outputs = [line.split("\n")[:-1] for line in cd_outputs]

dir_sizes = defaultdict(list)

for cd_part in cd_outputs:
    match cd_part[0]:
        case "/":
            p = Path("/")
        case "..":
            p = p.parent
        case other:
            p = p / cd_part[0]

    if "$ ls" in cd_part:
        ls_range_start = cd_part.index("$ ls") + 1
        ls_info = cd_part[ls_range_start:]
        file_sizes = [int(line.split(" ")[0]) for line in ls_info if line[0] not in ["$", "d"]]
        p_copy = p
        while p_copy.name != "":
            dir_sizes[p_copy.as_posix()].append(sum(file_sizes))
            p_copy = p_copy.parent
        dir_sizes[p_copy.as_posix()].append(sum(file_sizes))

total_dir_sizes = {dir_path: sum(dir_szs) for dir_path, dir_szs in dir_sizes.items()}
# part 1
print(sum(val for val in total_dir_sizes.values() if val < 100000))

total_disk_space = 70000000
needed_space = 30000000

total_space_used = total_dir_sizes["/"]
space_left = total_disk_space - total_space_used
to_be_deleted = needed_space - space_left

viable_dir_sizes = [val for val in total_dir_sizes.values() if val > to_be_deleted]

# part 2
print(min(viable_dir_sizes))
