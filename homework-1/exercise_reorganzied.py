from __future__ import annotations

from collections import Counter, defaultdict, deque
from typing import Iterable, List, Dict, Set


# =========================
# Exercise 1
# =========================

def count_positive_negative(numbers: Iterable[int]) -> tuple[int, int]:
    """Count how many positive and negative numbers are in the given iterable.
    :param numbers:
    :return:
    """
    positive_count = 0
    negative_count = 0

    for number in numbers:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

    return positive_count, negative_count


def run_exercise_1() -> None:
    data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
    pos, neg = count_positive_negative(data1)
    print("Exercise 1:")
    print(f"Positive number count: {pos}")
    print(f"Negative number count: {neg}\n")


# =========================
# Exercise 2
# =========================

def elements_with_frequency_greater_than_k(numbers: List[int], k: int) -> List[int]:
    """
    Return all distinct elements whose frequency in the list is greater than k.
    Uses Counter for efficiency instead of list.count() in a loop.
    """
    freq = Counter(numbers)
    return [num for num, count in freq.items() if count > k]


def run_exercise_2() -> None:
    data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
    k = 3
    solution = elements_with_frequency_greater_than_k(data2, k)
    print("Exercise 2:")
    print(f"Data2: {data2}")
    print(f"Solution (freq > {k}): {solution}\n")


# =========================
# Exercise 3
# =========================

def strongest_neighbours(numbers: List[int]) -> List[int]:
    """
    For each adjacent pair in the list, return the maximum of the two.
    Example: [4, 5, 6] -> [5, 6]
    """
    result: List[int] = []
    for i in range(len(numbers) - 1):
        result.append(max(numbers[i], numbers[i + 1]))
    return result


def run_exercise_3() -> None:
    data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
    solution = strongest_neighbours(data3)
    print("Exercise 3:")
    print(f"Data3: {data3}")
    print(f"Solution: {solution}\n")


# =========================
# Exercise 4
# =========================

def all_arrangements_three_digits(digits: List[int]) -> List[tuple[int, int, int]]:
    """
    Return all permutations of three distinct digits.
    Example: [1,2,3] -> (1,2,3), (1,3,2), (2,1,3), ...
    """
    arrangements: List[tuple[int, int, int]] = []
    for i in range(len(digits)):
        for j in range(len(digits)):
            for k in range(len(digits)):
                if i != j and j != k and i != k:
                    arrangements.append((digits[i], digits[j], digits[k]))
    return arrangements


def run_exercise_4() -> None:
    data4 = [1, 2, 3]
    arrangements = all_arrangements_three_digits(data4)
    print("Exercise 4:")
    print(f"Data4: {data4}")
    for triple in arrangements:
        print(triple)
    print()


# =========================
# Exercise 5
# =========================

def append_rows(list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
    """
    Given two 'matrix-like' lists (list of lists), append each row of list2
    to the corresponding row of list1.

    If they have different number of rows, extra rows are ignored.
    """
    for row1, row2 in zip(list1, list2):
        row1.extend(row2)
    return list1


def run_exercise_5() -> None:
    data5_list1 = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
    data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

    result = append_rows(data5_list1, data5_list2)
    print("Exercise 5:")
    print(f"Solution: {result}\n")


# =========================
# Exercise 6
# =========================

def numbers_divisible_by_7_not_5(start: int, end: int) -> List[int]:
    """
    Find numbers between start and end (inclusive) that are divisible by 7
    but not multiples of 5.
    """
    result: List[int] = []
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 != 0:
            result.append(i)
    return result


def run_exercise_6() -> None:
    result = numbers_divisible_by_7_not_5(2000, 3200)
    # Join into comma-separated string
    output = ",".join(str(x) for x in result)
    print("Exercise 6:")
    print(f"Solution: {output}\n")


# =========================
# Exercise 7
# =========================

def all_digits_even(number: int) -> bool:
    """
    Return True if every digit in the number is even.
    Example: 2480 -> True, 2461 -> False.
    """
    if number == 0:
        return False

    while number > 0:
        digit = number % 10
        if digit % 2 != 0:
            return False
        number //= 10
    return True


def numbers_with_all_even_digits(start: int, end: int) -> List[int]:
    """Return all numbers in [start, end] where every digit is even."""
    return [i for i in range(start, end + 1) if all_digits_even(i)]


def run_exercise_7() -> None:
    result = numbers_with_all_even_digits(1000, 3000)
    output = ",".join(str(x) for x in result)
    print("Exercise 7:")
    print(f"Solution: {output}\n")


# =========================
# Exercise 8 – Word chain
# =========================

def load_words(filename: str, limit: int | None = None) -> Set[str]:
    """
    Load words from a file, one per line, keeping only words of length >= 3.
    If limit is given, stop after that many words (helps avoid memory issues).
    """
    candidate_words: Set[str] = set()
    with open(filename, encoding="utf-8") as f:
        for count, line in enumerate(f, start=1):
            word = line.strip().lower()
            if len(word) >= 3:
                candidate_words.add(word)
            if limit is not None and count >= limit:
                break
    return candidate_words


def build_prefix_map(words: Set[str]) -> Dict[str, List[str]]:
    """
    Build a mapping from 2-letter prefix -> list of words starting with that prefix.
    Example: 'pa' -> ['paper', 'panda', 'party', ...]
    """
    prefix_map: Dict[str, List[str]] = defaultdict(list)
    for word in words:
        prefix = word[:2]
        prefix_map[prefix].append(word)
    return prefix_map


def build_chain(parent: Dict[str, str | None], goal: str) -> List[str]:
    """Reconstruct the chain from start to goal using the parent links."""
    chain: List[str] = []
    w: str | None = goal
    while w is not None:
        chain.append(w)
        w = parent[w]
    chain.reverse()
    return chain


def shortest_chain(start: str, goal: str, prefix_map: Dict[str, List[str]]) -> List[str] | None:
    """
    Find the shortest chain of words from start to goal such that:
    - Each word has at least 3 letters.
    - Last 2 letters of a word == first 2 letters of the next word.
    Uses BFS over an implicit graph defined by prefix_map.
    """
    start = start.lower()
    goal = goal.lower()

    if start == goal:
        return [start]

    queue: deque[str] = deque([start])
    visited: Set[str] = {start}
    parent: Dict[str, str | None] = {start: None}

    while queue:
        current = queue.popleft()
        suffix = current[-2:]  # last 2 letters of current word
        candidates = prefix_map.get(suffix, [])

        for nxt in candidates:
            if nxt in visited:
                continue

            visited.add(nxt)
            parent[nxt] = current

            if nxt == goal:
                return build_chain(parent, goal)

            queue.append(nxt)

    # If we exit the loop, there is no path
    return None


def run_exercise_8() -> None:
    # For testing: a small in-memory "dictionary"
    words: Set[str] = {
        "pen",
        "encroach",
        "chutzpa",
        "paper",
        "enter",
        "end",
        "panda",
        "pencil",
        "party",
        "pearl",
        "early",
    }

    # If you later want to load from a big file, use:
    # words = load_words("wordsEn.txt", limit=60000)

    prefix_map = build_prefix_map(words)

    start = input("Enter start word: ").strip().lower()
    goal = input("Enter goal word: ").strip().lower()

    if len(start) < 3 or len(goal) < 3:
        print("Words must have at least 3 letters.")
        return

    if start not in words or goal not in words:
        print("Start or goal word is not in the dictionary.")
        return

    chain = shortest_chain(start, goal, prefix_map)

    if chain is None:
        print("No chain found.")
    else:
        print("The shortest chain is:")
        for word in chain:
            print(word)


# =========================
# Main entry-point
# =========================

def main() -> None:
    """Run all exercises, then the interactive word-chain exercise."""
    run_exercise_1()
    run_exercise_2()
    run_exercise_3()
    run_exercise_4()
    run_exercise_5()
    run_exercise_6()
    run_exercise_7()
    run_exercise_8()


if __name__ == "__main__":
    main()
