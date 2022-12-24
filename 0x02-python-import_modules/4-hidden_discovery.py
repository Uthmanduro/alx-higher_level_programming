#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for lines in dir(hidden_4):
        if lines.startswith("__"):
            continue
        print(lines)
