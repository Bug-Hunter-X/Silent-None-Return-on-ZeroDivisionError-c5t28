# Silent None Return on ZeroDivisionError in Python

This repository demonstrates an uncommon coding error in Python: a function silently returning `None` when a `ZeroDivisionError` occurs, instead of raising the exception.  This can be problematic as calling functions may not anticipate `None` as a possible return value. 

**The Bug:**
The `bug.py` file contains a function that divides two numbers. If a `ZeroDivisionError` happens, it prints an error message to the console but then returns `None`. This is different from the common practice of raising the exception.  This can cause unexpected behavior if the calling code doesn't specifically check for `None` as a return value.

**The Solution:**
The `bugSolution.py` file shows a corrected version where the function raises the `ZeroDivisionError` instead of silently returning `None`. This allows calling functions to handle the error gracefully.