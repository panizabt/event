import re

def no_numbers(prompt):
    if type(prompt) == str and re.match('^[a-zA-z\s]{3,20}$', prompt):
        return prompt

def no_space(prompt):
    if type(prompt) == str and re.match('^\w{3,20}$', prompt):
        return prompt

def password_validator(prompt):
    if type(prompt) == str and re.match('^.*(?=a-zA-Z0-9)\w{5,20}$', prompt):
        return prompt
    else:
        return 0
