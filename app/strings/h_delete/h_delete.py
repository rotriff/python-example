def h_delete(h_string: str):
    if not isinstance(h_string, str):
        raise TypeError(f'Argument "h_string" must be string, not {type(h_string)}')
    h = []
    new_h_string = h_string.lower()
    for i in range(len(new_h_string)):
        if new_h_string[i] == "h":
            h.append(i)
    if h != []:
        return new_h_string.replace(new_h_string[h[0]:h[-1] + 1], "")
    else:
        return h_string
