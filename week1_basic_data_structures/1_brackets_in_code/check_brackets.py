# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left: str, right: str) -> bool:
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str) -> int:
    """
    Given a str, check if the brackets all match. If not, returns the index of the first unmatched
    closing bracket (first priority), otherwise returns the index of the first unmatched opening
    bracket.

    For example: ']()', should returns 1, the unmatched closing bracket is in the first position.
        '{}([]', should return 3, '(', the unmatched opening bracket is in the 3rd position.
        '{}([]}', should return 6, in this case, the string has both unmatched opening and closing
        brackets. The unmatched closing bracket '}' has higher priority.

    Returns:
        int, if there is no mismatch return 0, otherwise returns the index (starting from 1) of
        the unmatched position.
    """

    opening_brackets_stack = []
    for i, element in enumerate(text):
        if element in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(element, i+1))

        if element in ")]}":
            # Process closing bracket, write your code here

            # no opening brackets exit to match closing bracket.
            if len(opening_brackets_stack) == 0:
                return i + 1

            open_bracket = opening_brackets_stack.pop()
            if not are_matching(open_bracket.char, element):
                return i + 1

    if len(opening_brackets_stack) == 0:
        return 0
    else:
        # all closing brackets are matched, but there are still
        # opening brackets left. Return the first unmatched opening bracket.
        return opening_brackets_stack[0].position


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == 0:
        print('Success')
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
