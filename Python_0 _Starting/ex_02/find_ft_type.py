

def all_thing_is_obj(object: any) -> int:
    try:
        if(str(object) == object): 
            print(object, "is in the kitchen : <class 'str'>")    
        elif (list(object) == object):
            print("List : <class 'list'>")
        elif (tuple(object) == object):
            print("Tuple : <class 'tuple'>")
        elif (set(object) == object):
            print("Set : <class 'set'>")
        elif (dict(object) == object):
            print("Dict : <class 'dict'>")
        else:
            print("Type not found")
    except:
        print("Type not found")
        return 42
    return 42
    
from find_ft_type import all_thing_is_obj
    
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)

all_thing_is_obj("Brian")
all_thing_is_obj("Toto")

print(all_thing_is_obj(10))


# $>python tester.py | cat -e
# List : <class 'list'>$
# Tuple : <class 'tuple'>$
# Set : <class 'set'>$
# Dict : <class 'dict'>$
# Brian is in the kitchen : <class 'str'>$
# Toto is in the kitchen : <class 'str'>$
# Type not found$
# 42$
# $>
