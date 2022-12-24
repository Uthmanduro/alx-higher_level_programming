#!/usr/bin/python3
"""
    Usage: ./100-my_calculator.py <a> operator <b>
"""
if __name__ == "__main__":
    import sys
    import calculator_1
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = ["+", "-", "*", "/"]
    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if sys.argv[2] == "+":
            result = calculator_1.add(int(sys.argv[1]), int(sys.argv[3]))
            print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")
        elif sys.argv[2] == "-":
            result = calculator_1.sub(int(sys.argv[1]), int(sys.argv[3]))
            print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")
        elif sys.argv[2] == "*":
            result = calculator_1.mul(int(sys.argv[1]), int(sys.argv[3]))
            print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")
        elif sys.argv[2] == "/":
            result = calculator_1.div(int(sys.argv[1]), int(sys.argv[3]))
            print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")
