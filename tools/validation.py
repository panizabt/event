import re

def no_numbers(prompt,message):
    if type(prompt) == str and re.match(r'^[a-zA-z\s]{3,20}$', prompt):
        return prompt
    else:
        raise ValueError(message)

def no_space(prompt,message):
    if type(prompt) == str and re.match(r'^\w{3,20}$', prompt):
        return prompt
    else:
        raise ValueError(message)


def password_validator(prompt, message):
    # if type(prompt) == str and re.match(r'^.*(?=a-zA-Z0-9)[\w\d]{5,20}$', prompt):
    if type(prompt) == str and re.match(r'^.*$', prompt):
        return prompt
    else:
        raise ValueError(message)