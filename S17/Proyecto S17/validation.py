def text_validation(text):
    return text is not None and text.strip() != ""


def amount_validation(amount):
    try:
        value = float(amount)
        return value > 0
    except:
        return False