# Technical HW: Stacks & Queues
Please complete the following 4 functions. You can test by running the `pytest` or `python3` commands:

* To run just the main code for one problem: `python3 reverse.py`
* To run the tests for one problem: `pytest reverse_test.py`
* To run all the tests prior to submission: `pytest`

### Files that should (& shouldn't!) be changed

You **SHOULD** implement your problem solutions in the following files:
* reverse.py
* matching.py
* generate_binary.py
* count_longest.py

You **SHOULD NOT** modify the following files:
* Queue.py
* Stack.py
* count_longest_test.py
* generate_binary_test.py
* matching_test.py
* reverse_test.py

Looking for additional practice problems to prepare for the exam?
* practice-problems.py

### General Hints
* _Thinking of using a loop? For loops are for strings, whiles are for Stacks & Queues!_
* _The only way to iterate / loop through the Stack or Queue you've been given in this assignment is to destroy it (i.e., make it empty)._

## Problem 1: reverse queue

Write a function ```reverse``` in python that takes a
queue as a parameter and returns a new queue in 
reverse order. Your solution _should not_ use
any built-in or library functions other than those in
the `Stack` and `Queue` classes provided.

| **Example call** | **Returns** |
| -------------- | --------- |
| `reverse( Q[1, 2, 3, 4] )` | `Q[4, 3, 2, 1]` |
| `reverse( Q[hello] )` | `Q[olleh]` |
| `reverse( Q[0] )` | `Q[0]` |

_Note:_ We are using the notation `Q[ ]` here to 
differentiate our queues from lists or arrays.

_**Hint**: use a stack to help! You can destroy the queue & make it empty!_

## Problem 2: brace matcher

Write a function `matcher` in python that takes a
string containing braces (`[{()}]`) as a parameter
and returns True if the braces are matched, and
False otherwise. The braces may be nested. 
Your solution _should not_ use
any built-in or library functions other than those in
the `Stack` and `Queue` classes provided.

| **Example call** | **Returns** |
| -------------- | --------- |
| `matcher("[()]")` | `True` |
| `matcher("[(")` | `False` |
| `matcher("hello")` | `True` |

_**Hint**: use a stack!_

## Problem 3: generate binary number strings

Write a function ```generate_binary_numbers``` that
takes a number _N_ as a parameter and returns a queue
of binary number strings from _1_ to _N_ _without_ 
using any built-in or library functions like `bin()`. 
In fact, your solution _should not_ use
any built-in or library functions other than those in
the `Stack` and `Queue` classes provided.
The front of the queue begins @ '1'. If _N_ is too 
small, return an empty queue. 

| **Example call** | **Returns** |
| -------------- | --------- |
| `generate_binary_numbers(2)` | `Q['1', '10']` |
| `generate_binary_numbers(3)` | `Q['1', '10', '11']` |
| `generate_binary_numbers(6)` | `Q['1', '10', '11', '100', '101', '110']` |

_**Hint**: use an extra queue to help!_

### Review: Binary Numbers

Recall that the typical numbers we are used to
working with every day are decimal numbers, or
base 10. By contrast, computers  natively work
with _**binary numbers**_, which are base 2.

To read binary numbers, begin writing the powers
of 2 from right to left:

| **Binary** | **Decimal** |
| -------------- | --------- |
|2<sup>3</sup> 2<sup>2</sup> 2<sup>1</sup> 2<sup>0</sup> | |
| `8 4 2 1` | |
| `. . . 1` | 1 |
| `. . 1 0` | 2 |
| `. . 1 1` | 3 |
| `. 1 0 0` | 4 |
| `. 1 0 1` | 5 |
| `. 1 1 0` | 6 |
| `. 1 1 1` | 7 |
| `1 0 0 0` | 8 |
| `1 1 0 0` | 12 |
| `1 1 1 1` | 15 |

_Note:_ The dots (`.`) should **not** be in your final
output, but are used here to align the numbers under
the appropriate power of 2.

## Problem 4: count the longest subsequence

Write a function ```count_longest``` that takes a
queue of characters as a parameter and returns the
length of the longest consecutive subsequence. For
example:

| **Example call** | **Returns** |
| -------------- | --------- |
| `count_longest( Q[h, e, l, l, o] )` | `2` |
| `count_longest( Q[m, m, m, m, m] )` | `5` |
| `count_longest( Q[h, e, e, e] )` | `3` |
| `count_longest( Q[ ] )` | `0` |

_**Hint**: you can destroy the queue & make it empty!_

Your solution _should not_ use
any built-in or library functions other than those in
the `Stack` and `Queue` classes provided.

## Getting started

### Develop online

Click the "Work in Repl.it" button. Edit the file. To run, see the commands below.

### Develop in PyCharm

With this option, you can develop on your laptop. 
You will need to install PyCharm (or another IDE),
git, and pytest. PyCharm has some built-in git 
support.

## Testing
Many of the tests are failing right now because the 
functions
aren't outputting the correct information. Fixing this
will make the tests pass & turn green.

### Setup
To use pytest on repl.it, install it first:

`pip3 install pytest`

To install pytest on the command line for running on a laptop (using a linux or unix based command-line like MacOS):

`sudo -H pip3 install pytest`

If using PyCharm, you may need to fix your project setup.
- Open the **Settings/Preferences | Tools | Python Integrated Tools** settings dialog.
- In the Default test runner field select **pytest**.
- Click OK to save the settings.

### Run commands
To run just the main code for one problem:

`python3 reverse.py`

To run the tests for one problem:

`pytest reverse_test.py`

To run all the tests prior to submission:

`pytest`
