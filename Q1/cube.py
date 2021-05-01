def volume(a):
    if type(a) not in [int, float]:
        raise TypeError("Intergers only.")
    if a > 0:
        return a ** 3
    if a < 0:
        raise ValueError("Positive integers only.")