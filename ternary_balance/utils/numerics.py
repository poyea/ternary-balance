from typing import List

class numerics(object):
    """Numeric utilities for solving the problem.
    """

    @staticmethod
    def plus_to_pos(original: List[int], position: int, k: int = 3) -> List[int]:
        """Recursive helper function to add one at a location of a list of (bit) integers
            representing a k-ary number.

        Args:
            original (List[int]): The list of (bit) integer to modify.
            position (int): The index or the position to add one.
            k (int): The base k used by the original list.

        Returns:
            The resulting list of (bit) integers after the operation.

            Notice that the returning and input lists are little endian.

        >>> numerics.plus_to_pos([0, 9, 9, 1], 1, 10)
        [0, 0, 0, 2]
        >>> numerics.plus_to_pos([0, 8, 0, 1], 1, 10)
        [0, 9, 0, 1]
        >>> numerics.plus_to_pos([0, 1], 0)
        [1, 1]
        >>> numerics.plus_to_pos([1, 0, 1, 2, 0, 1], 3)
        [1, 0, 1, 0, 1, 1]
        >>> numerics.plus_to_pos([0], 0, 3)
        [1]
        >>> numerics.plus_to_pos([0, 1, 0, 0, 1], 2)
        [0, 1, 1, 0, 1]
        """
        if position == len(original):
            original.append(1)
        elif original[position] < k - 1:
            original[position] += 1
        else:
            original[position] = 0
            original = numerics.plus_to_pos(original, position + 1)
        return original

    @staticmethod
    def dec_to_k(number: int, k: int = 3) -> List[int]:
        """Helper function to transform a decimal into a k-nary.

        Args:
            number (int): The decimal to be transformed
            k (int): The target base.

        Returns:
            A list of integers, consisting of 0, 1,..., k-1. For example,

            [1, 0, 2, 0, 1] for a ternary number after transformation.

            Notice that the returning list is little endian.

        >>> numerics.dec_to_k(1080, 10)
        [0, 8, 0, 1]
        >>> numerics.dec_to_k(100)
        [1, 0, 2, 0, 1]
        >>> numerics.dec_to_k(3, 3)
        [0, 1]
        >>> numerics.dec_to_k(307, 3)
        [1, 0, 1, 2, 0, 1]
        >>> numerics.dec_to_k(0)
        [0]
        >>> numerics.dec_to_k(18, 2)
        [0, 1, 0, 0, 1]
        """
        lst = []
        while number:
            lst.append(number % k)
            number //= k
        return lst if len(lst) else [0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
