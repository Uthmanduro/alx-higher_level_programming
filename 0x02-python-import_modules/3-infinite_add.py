#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = 1
    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[index])
        index += 1
    print(sum)
