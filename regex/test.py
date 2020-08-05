import regex
import re


def get_variables(text):
    """
    Takes as input a string and returns a list of all valid replace fields, ie.
    Input "${first} ${second hey}   ${third" will return ['${first}', '${second hey}']
    :param text: String where we search after replace fields
    :return: List of valid replace fields
    """
    regex = re.compile(r'(\$\{.*?\})')
    return regex.findall(text)


print(get_variables('${first} ${second hey}   ${t'))  # ['${first}', '${second hey}']
