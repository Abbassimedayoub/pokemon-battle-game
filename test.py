import time  # time manipulation
import sys  # access to the stdout


def delay_print(s):
    for c in s[::-1]:
        print(c, end='', flush=True)
        time.sleep(0.05)
    print()


def main():
    delay_print("ayoub is the best on in all over the world ")


if __name__ == "__main__":
    main()
