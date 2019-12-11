HTML_SPACE = '&nbsp;'


def prefill_with_character(value, column_length = 4, fill_char = HTML_SPACE):
    return str(value).rjust(column_length, " ").replace(" ", fill_char)
