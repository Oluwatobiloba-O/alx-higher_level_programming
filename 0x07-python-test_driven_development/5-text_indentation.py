#!/usr/bin/python3

def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :.

    Args:
        character: containing the characters.
        count: keeps track of the number of loops
        lines: list containing the splitted string

    Raises:
        Text must be a string
        Input must not be an empty string
    """

    if type(text) is not str or text is None:
        raise TypeError("text must be a string")
    if not text.strip():
        raise ValueError("input must not be an empty string")
    
    characters = ['.', '?', ':']

    for char in characters:
        text = text.replace(char + ' ', char + '\n')

    lines = text.split('\n')

    count = 0

    for line in lines:
        stripped_line = line.strip()
        count += 1
        if stripped_line and count < len(lines):
            print(stripped_line)
            print()
        else:
            print(stripped_line, end="")