from typing import List, Set
from ternary_balance.utils.numerics import *


class ternary_balance(object):
    """A solver class, wrapped with input and output, for ternary balance problem.

    Given a valid integer value, balance the number on 2 cups
    with ternary weights in the set {1, 3, 9, 27, 81, 243, 729, ...}.

    If the input is not valid, a default value of 100 will be used.

    """

    def solve(self) -> None:
        """The solver function for the problem.

        Typical usage example:

        >>> from ternary_balance.solver import ternary_balance
        >>> solver = ternary_balance()
        >>> solver.solve()
        """
        number = self.__request_num()
        list_of_bits = numerics.dec_to_k(number)
        location = set()
        for i in range(len(list_of_bits)):
            if list_of_bits[i] == 2:
                location.add(i)
                list_of_bits[i] -= 1
                list_of_bits = numerics.plus_to_pos(list_of_bits, i + 1)
        self.__display_result(list_of_bits, location, number)

    def __request_num(self) -> int:
        """Input handler for the class.

        Returns:
            A number that the user gives in the stdin or 100 if it is not valid.
        """
        number = input("Enter an integer to balance: ")
        return int(number) if number.isdigit() else 100

    def __display_result(
        self, result: List[int], location: Set[int], number: int
    ) -> None:
        """Output handler for the class. This will display the result to stdout.

        Args:
            result (List[int]): The list of (bit) integers that represents the final state
                of the balance system.
            location (Set[int]): The set containing the information of modified positions.
            number (int): The original number.
        """
        print(
            f"To weigh {number} in the left cup of balance, one needs to place the ternary weights "
            "in the left (L) and right (R) cups as follow - "
        )
        for i in range(len(result)):
            if result[i] == 1:
                if i in location:
                    print(f"L: {pow(3, i)}")
                else:
                    print(f"R: {pow(3, i)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
