from typing import List


def generate_10_numbers_from_0_until_100() -> List[int]:
    import random
    numbers = random.sample(range(0, 99, 2), 10)
    return numbers


def print_list(numbers: List[int]):
    print(numbers)


def sort_in_ascending_order(numbers: List[int]) -> List[int]:
    newnumbers = sorted(numbers)
    return newnumbers


def remove_content_which_number_is_under_50(numbers: List[int]) -> List[int]:
    newnumbers = ([s for s in numbers if not s < 50])
    print(newnumbers)


if __name__ == '__main__':
    import random

    numbers = random.sample(range(0, 99, 2), 10)
    print(numbers)
    print(sorted(numbers))
    newnumbers = ([s for s in numbers if not s < 50])
    print(newnumbers)