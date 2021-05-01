def avg(lst):
    if (len(lst)) == 0:
        raise ValueError("Cannot divide by 0 (zero).")
    avg = sum(lst) / len(lst)
    return avg
