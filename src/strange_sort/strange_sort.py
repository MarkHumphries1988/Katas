def strange_sort(*args, desc=True):
    return sorted(args, key=lambda x: (-len(x), x.lower()), reverse=not desc)
    pass
