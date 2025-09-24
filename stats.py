from typing import Dict, List, Any


def count_words(text: str) -> int:
    if type(text) != str:
        raise TypeError("text must be str")
    return text.split().__len__()


def count_unique_chars(text: str) -> Dict[str, int]:
    if type(text) != str:
        raise TypeError("text must be str")
    result = {}
    for char in text.lower():
        if char in result:
            result[char] += 1
            continue
        result[char] = 1
    return result


def sort_on(item):
    return item["num"]


def sort_chars_by_count(chars_dict: Dict[str, int]) -> List[Dict[str, Any]]:
    char_count_list = []
    for char in chars_dict:
        char_count_list.append({"char": char, "num": chars_dict[char]})
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list
