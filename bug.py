def function_with_uncommon_bug(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

# The bug is that the function will return None if there is an error, 
# instead of raising an exception which is more common approach.
# This could cause unexpected behavior in other parts of the code that 
# are not explicitly handling the None return value.
# This also lacks proper error handling in general.