# def sum_text(input_string) -> str:
#     caunt_leters = 0
#     for char in input_string:
#         if char.isalpha():
#             caunt_leters += 1
#     print(caunt_leters)

# sum_text ("Test")


# text = input("enter_string")
# def count_letters(in_string: str):    
#     return len(in_string.replace(" ", ""))

# print(count_letters(text))

# Create a function that adds a string ending to each member in a list.
# Sukurkite funkciją, kuri prie kiekvieno sąrašo nario prideda eilutės galūnę.

def sum_text(input_list: str, ending: str) -> str:
   return [word + ending for word in input_list]
        
input_list = ["car", "truck"]
ending = "nice"
rezult_list = sum_text(input_list,ending)
print(rezult_list)


# def add_ending_to_strings(input_list, ending):
#     return [word + ending for word in input_list]
# input_list = ["apple", "banana", "cherry"]
# ending = "_fruit"
# result_list = add_ending_to_strings(input_list, ending)
# print(result_list)


# def add_start_to_string ( first: str, input_list: str) -> str:
#     return [first + word for word in input_list]
# input_list = ["car"]
# first = "new"
# result_list = add_start_to_string(first,input_list)
# print(result_list)


# Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.
# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.

