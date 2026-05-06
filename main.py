def main():
    print("Hello from dsc190-a5!")
    import os          # F401: unused import
    import sys         # F401: another unused import
    x=1+1              # E225: missing whitespace around operator
    y = [1,2,3]        # E231: missing whitespace after comma
    def foo( ):        # E211: whitespace before '('
        pass


if __name__ == "__main__":
    main()
