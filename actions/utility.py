def get_subdata(s):
    symbol = s[0]
    data = 0
    i = 1
    while s[i] != '\n':
        if i == len(s) - 1:
            return s, None, None
        data = data * 10 + int(s[i])
        i += 1
    s = s[i + 1:]
    return s, symbol, data
