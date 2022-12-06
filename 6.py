from pathlib import Path

inhalt = (Path(__file__).parent / "input").read_text()[:-1]


def find_marker(string: str, length: int):
    i = 0
    while len(set(string[i:i + length])) < length:
        i += 1
    return i + length


print(find_marker(inhalt, 4))
print(find_marker(inhalt, 14))
