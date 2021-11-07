def calculator(x):
    if -10 <= x <= -2:
        return x * -x
    elif x == -1:
        return 1 / 128
    elif -2 < x < 8:
        return (1 - x) / (1 + x)
    elif x == 8:
        return 1 / 128
    elif 8 < x <= 35:
        return abs(x - 12)
    else:
        return 1 / 128
