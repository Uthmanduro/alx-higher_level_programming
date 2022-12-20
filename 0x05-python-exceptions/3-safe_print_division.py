#!/usr/bin/python3
def safe_print_division(a, b):
    div = None
    try:
        div = a / b
        return div
    except (ValueError, ZeroDivisionError):
        return None
    finally:
        print("Inside result: {}".format(div))
