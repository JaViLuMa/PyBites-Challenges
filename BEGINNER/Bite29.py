import string

def get_index_different_char(chars):
    alphanumeric = list(string.ascii_letters + string.digits)
    
    alpha = []
    nonAlpha = []
    
    for index, char in enumerate(chars):
        if type(char) is int or char.lower().isalpha():
            alpha.append(index)
        else:
            nonAlpha.append(index)
    
    return nonAlpha[0] if len(alpha) > len(nonAlpha) else alpha[0]
