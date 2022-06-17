from typing import List

def sat198(ordered: List[int], nums=[1, 0, -1, -100, 10, 14, 235251, 11, 10000, 2000001, -155]):
    digit_sums = [sum(int(c) for c in str(n) if c != "-") for n in ordered]
    return sorted(ordered) == sorted(nums) and digit_sums == sorted(digit_sums)
def sol198(nums=[1, 0, -1, -100, 10, 14, 235251, 11, 10000, 2000001, -155]):
    """Sort the numbers by the sum of their digits

    [17, 21, 0] => [0, 17, 21]
    """
    return sorted(nums, key=lambda n: sum(int(c) for c in str(n) if c != "-"))
# assert sat198(sol198())
