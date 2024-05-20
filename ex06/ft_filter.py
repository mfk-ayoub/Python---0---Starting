def filter(fun, text):
    if fun:
        return (item for item in text if fun(item))
    return (item for item in text if item)