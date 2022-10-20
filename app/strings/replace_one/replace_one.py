def replace_one(phrase: str):
    if not isinstance(phrase, str):
        raise TypeError(f'Argument "phrase" must be string, not {type(phrase)}')
    for character in phrase:
        if character == "1":
            new_phrase = phrase.replace("1", "one")
            return new_phrase
        else:
            return phrase
