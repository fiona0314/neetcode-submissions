from typing import List

def contains_duplicate(words: List[str]) -> bool:
    words_len = len(words)
    words_set_len = len(set(words))
    if words_len > words_set_len:
        return True
    else:
        return False


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
