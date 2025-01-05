
import sys
def main(*args):
    if len(*args) != 1:
        print ("AssertionError: more than one argument is provided")
        return 1
    elif args[0].isdigit() == False:
        #(args[0][0] != '-' & args[0][1:].isdigit() == False):
        print ("AssertionError: argument is not an integer")
        print (args[0][0])
        return 1


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