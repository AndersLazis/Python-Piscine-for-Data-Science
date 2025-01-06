
import sys


def check_number(number) -> str:
    """
    Returns the result of check.
    """
    try:
        number = int(number)
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit(1)
    if (number % 2 != 0):
        return ("I'm Odd.")
    else:
        return ("I'm Even.")


def main(*args):
    """
    Main function
    """
    try:
        if len(args) > 1:
            raise AssertionError("AssertionError: more than one argument is provided")
        elif len(args) == 0:
            return 1
    except AssertionError as e:
        print(e)
        return 1 
          
    print(check_number(args[0]))
    #print (main.__doc__)
    #print (check_number.__doc__)


if __name__ == "__main__":
    main(*sys.argv[1:])


# $> python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# AssertionError: more than one argument is provided
# $>