"""Dictionary Main"""

__author__: str = "730661635"

original: dict[str, str] = {"a": "b", "c": "d"}
new: dict[str, str] = {"b": "a", "d": "c"}


def invert(original: dict[str, str]) -> dict[str, str]:
    """inverts the keys and the values"""
    inverted: dict[str, str] = {}
    for key in original:
        if original[key] in inverted:
            raise KeyError
        inverted[original[key]] = key
    return inverted


print(invert(original))


def count(values: list[str]) -> dict[str, int]:
    """counts the number of times each value appears"""
    empty_dict: dict[str, int] = {}
    for element in values:
        if element in empty_dict:
            empty_dict[element] += 1
        else:
            empty_dict[element] = 1
    return empty_dict


def favorite_color(names_colors: dict[str, str]) -> str:
    """returns the most popular color"""
    empty_colors: dict[str, int] = {}
    color: str = ""
    max = 0
    for n in names_colors:
        if names_colors[n] in empty_colors:
            empty_colors[names_colors[n]] += 1
        else:
            empty_colors[names_colors[n]] = 1
    for n in empty_colors:
        if empty_colors[n] > max:
            max = empty_colors[n]
            color = n
    return color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """bins a list of strings into a dictionary"""
    empty: dict[int, set[str]] = {}
    for word in strings:
        if len(word) in empty:
            empty[len(word)].add(word)
        else:
            empty[len(word)] = {word}
    return empty
