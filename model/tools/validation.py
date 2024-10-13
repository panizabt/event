import re

class Validation:
    pass
# def no_numbers(prompt,message):
#     if type(prompt) == str and re.match('^[a-zA-z\s]{3,20}$', prompt):
#         return prompt
#     else:
#         raise ValueError(message)
#
# def no_space(prompt,message):
#     if type(prompt) == str and re.match('^\w{3,20}$', prompt):
#         return prompt
#     else:
#         raise ValueError(message)
#
#
 def password_validator(prompt):
     if type(prompt) == str and re.match(r'^.*(?=a-zA-Z0-9)\w{5,20}$', prompt):
         return prompt
     else:
         raise ValueError(message)