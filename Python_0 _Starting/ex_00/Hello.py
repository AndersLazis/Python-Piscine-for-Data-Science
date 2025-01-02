
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

#List:
ft_list[-1] = "World!"

#Tuple:
tmp_list = list(ft_tuple)
tmp_list[-1] = "Deutscland!"
ft_tuple = tuple(tmp_list)

#Set:
ft_set.remove("tutu!")
ft_set.add("Wolfsburg!")

#Dictionary:
ft_dict["Hello"] = "42Wolfsburg!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# Expected output:
# $>python Hello.py | cat -e
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$
# $>