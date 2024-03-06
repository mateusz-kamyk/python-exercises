import math

def calculate_sine(value, unit):
    if unit == "d":
        result = math.sin(math.radians(value))
    elif unit == "r":
        result = math.sin(value)
    else:
        print("You've provided wrong unit.")
    return result

def calculate_cosine(value, unit):
    if unit == "d":
        result = math.cos(math.radians(value))
    elif unit == "r":
        result = math.cos(value)
    else:
        print("You've provided wrong unit.")
    return result

def calculate_tangent(value, unit):
    if unit == "d":
        result = math.tan(math.radians(value))
    elif unit == "r":
        result = math.tan(value)
    else:
        print("You've provided wrong unit.")
    return result

def calculate_cotangent(value, unit):
    if unit == "d":
        result = 1 / math.tan(math.radians(value))
    elif unit == "r":
        result = 1 / math.tan(value)
    else:
        print("You've provided wrong unit.")
    return result
