def replaceall(text, dictionary):
    for word, replacement in dictionary.items():
        text = text.replace(word, replacement).lower()

    text = "_".join(text.split())
    return text

def try_float(x):
    if x is not None:
        try:
            return float(x)
        except:
            return float(0)
    else:
        return float(0)

def try_string(x):
    if x is not None:
        try:
            return str(x)
        except:
            return ''
    else:
        return ''
