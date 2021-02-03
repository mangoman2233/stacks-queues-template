# PRACTICE: What is the output &
# ADT look like after every line?

from Queue import Queue
from Stack import Stack


def stack_first():
    s = Stack()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 9):
        print("Push ", str(i) + ": ", end="")
        s.push(i)
        s.print()
    print("Peek:", s.peek())
    for i in range(3):
        print("Pop: ", s.pop(), "-- ", end="")
        s.print()
    print("Peek:", s.peek())
    print("Is empty?", s.is_empty())


def stack_test(s_str, op_str):
    s = Stack([])
    i = 0
    for op in op_str:
        if op == "u":
            if i < len(s_str):
                print("Push  ", s_str[i] + ":  ", end="")
                s.push(s_str[i])
                s.print()
                i += 1
        elif op == "k":
            print("Peek: ", s.peek())
        elif op == "o":
            print("Pop:  ", s.pop(), "- ", end="")
            s.print()
        elif op == "i":
            print("Is empty?", s.is_empty())
        else:
            print("ERROR: unknown operation", op)


def queue_first():
    q = Queue()
    q.print()
    print("Is empty?", q.is_empty())
    for i in range(1, 9, 2):
        print("Enq   ", str(i) + ":  ", end="")
        q.enq(i)
        q.print()
    print("Front:", q.front())
    for i in range(4):
        print("Deq:  ", q.deq(), "- ", end="")
        q.print()
    print("Front:", q.front())
    print("Is empty?", q.is_empty())


def queue_test(q_str, op_str):
    q = Queue([])
    i = 0
    for op in op_str:
        if op == "e":
            if i < len(q_str):
                print("Enq   ", q_str[i] + ":  ", end="")
                q.enq(q_str[i])
                q.print()
                i += 1
        elif op == "f":
            print("Front:", q.front())
        elif op == "d":
            print("Deq:  ", q.deq(), "- ", end="")
            q.print()
        elif op == "i":
            print("Is empty?", q.is_empty())
        else:
            print("ERROR: unknown operation", op)


def main():
    print("=" * 10, "Problem Queue 1", "=" * 10)
    queue_first()
    print("=" * 10, "Problem Stack 1", "=" * 10)
    stack_first()
    print("=" * 10, "Problem Queue 2", "=" * 10)
    queue_test("hello there", "ieedfeefdeeeifeeddeefdddi")
    print("=" * 10, "Problem Stack 2", "=" * 10)
    stack_test("hello!", "iuuokuukouuuikuuoouukoooi")
    print("=" * 10, "Problem Queue 3", "=" * 10)
    queue_test("hello!", "ieedfeefdeeeifeeddeefdddi")
    print("=" * 10, "Problem Stack 3", "=" * 10)
    stack_test("hello there", "iuuokuukouuuikuuoouukoooi")


if __name__ == "__main__":
    main()
