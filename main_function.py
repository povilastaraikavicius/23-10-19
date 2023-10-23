# from typing import Optional, Union, List


# def some_one(a:Union[int,float])-> Union[int,str]:
#     if type(a) == "int":
#         return a
#     else:
#         return str(a)
    
# def optinal_type(a:Union[int,float])-> Optional (int):
#     if type(a)== "int":
#         return a
#         return None
#     my_list: List[Union[str,int, float]]= ["fddd", 1, 1.56]

#     my_dict: Dict [str, Optional (Union{int, float})] = {"a": 1, "b": 1.23, "c": None}
    
# Create a function that returns only strings with unique characters.
# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias eilutes.


# def unique_characters(input_string:str)-> str:
#     return set [input_string] 

# input_string = "welcome",


# rezult_list = unique_characters(set(input_string))

# print(rezult_list)



# def sum_text(input_list: list , ending: str) -> list:
#    return [word + ending for word in input_list]
        
# input_list = ["car", "truck"]
# ending = "nice"
# rezult_list = sum_text(input_list,ending)
# print(rezult_list)

# from typing import List


# simbol = input("please enter word with spec simbol:  ")

# def find_word(in_text: str)-> List[str]:
#     unique_char: List [str] = ["!","@","$","%","^","&","*","+","-","_"]
#     splited_words: List [str] = in_text.split(" ")
#     unique_words: List [str] = [word for word in splited_words if any(simb in word for simb in unique_char)]
#     return unique_words

# print(find_word(simbol))
 
# Generate a dictionary of 10 keys being 1,2,3...10 each of them should store a value of random integer number from 1 to 100.



# Task nr.1: 
# Create a mini program that takes 10 random numbers in
# one input ("1,2,5 76,89 ...etc")Write functions to: calculate their sum, 
# multiplication of highest and lowest numbersand the function
# which makes a new string where numbers are positioned from highest to lowest.

# Sukurkite mini programą, kuri užima 10 atsitiktinių skaičių
# viena įvestis ("1,2,5 76,89 ... ir tt")Rašykite funkcijas, kad: apskaičiuotumėte jų sumą, 
# didžiausių ir mažiausių skaičių daugybir 
# funkcija kuris sukuria naują eilutę, kurioje skaičiai yra išdėstyti nuo didžiausio iki žemiausio.


def find_sum(number_list: [int]) -> int:
    return sum(number_list)
numbers_input = input("Please enter 10 random numbers: ")
number_list = [int(number) for number in numbers_input.split(",")]
# if len(number_list) == 10:
result = find_sum(number_list)
print("Sum of the numbers:", result)
# else:
#     print("Please enter exactly 10 numbers.")

max_number = max(number_list)
min_number = min(number_list)
print("multiplication of highest and lowest number:",max_number * min_number)

sorted_num = sorted(number_list)
print("from highest to lowest nuber: ", sorted_num)
