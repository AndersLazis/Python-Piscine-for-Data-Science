def NULL_not_found(object: any) -> int:
    try:
        if object != object:
            print("Cheese: nan <class 'float'>")
        elif object == None:
            print("Nothing: None <class 'NoneType'>")       
        elif object == '':
            print("Empty: <class 'str'>")
        elif (object == 0 & ((int(object) == object) |
                             (float(object) == object))):
            print("Fake: False <class 'bool'>")
        elif object == 0:
            print("Zero: 0 <class 'int'>")                  
    except:
        print("Type not found")
        return 1
    return 0
               
        
    




#Expected output:

# $>python tester.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
# $>