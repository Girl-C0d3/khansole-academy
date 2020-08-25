"""
File: khansole_academy.py
-------------------------
This programme will ask the user to input answers to randomly generated arithmetic problems.
The programme terminates when the user has answered 3 problems correctly in a row.
"""

import random


def main():
    correct_answers = 0
# programme runs whilst correct answers in a row is below 3
    while correct_answers < 3:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        total = num1 + num2
        print("what is " + str(num1) + " + " + str(num2) + "?")
        answer = int(input("Your answer: "))

        if answer == total:
            # if the user answers correctly, 1 is added to the previous value for correct answers
            correct_answers += 1
            print("Correct! You have got " + str(correct_answers) + " correct in a row")
            print("")
        else:
            print("Incorrect. The expected answer was " + str(total))
            print("")
            # If user gives an incorrect answer, correct answers is reset to 0
            correct_answers = 0
# Once the user has answered 3 problems correctly in a row, the while loop is exited and the programme terminates by
# printing a congratulations statement
    if correct_answers == 3:
        print("congratulations! You mastered addition!")


if __name__ == '__main__':
    main()