import re

def count_indents(text):
    return re.search("[^ ]", text).start()
