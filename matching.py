# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Jacob Jeong
# ASSIGNMENT:   Project 2: Stacks & Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise
def matcher(str):
    stack = []
    for i in str:
        if i in '[({':
            stack.append(i)
        elif i in '])}':
            if len(stack) == 0:
                return False
            if '])}'.index(i) != '[({'.index(stack.pop()):
                return False
    return len(stack) == 0


def main():
    print("matcher: ", matcher("[()]"))

# Don't run main on import
if __name__ == "__main__":
    main()

