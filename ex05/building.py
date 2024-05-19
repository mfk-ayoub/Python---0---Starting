import sys


def building(name):
    c_lower = 0
    c_upper = 0
    c_digit = 0
    p_marks = 0
    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for i in name:
        if i.islower():
            c_lower += 1
        elif i.isupper():
            c_upper += 1
        elif i.isdigit():
            c_digit += 1
        elif i in punctuation_characters:
            p_marks += 1

    print(f"The text contains {len(name) + 1} characters:")
    print(f"{c_upper} upper letters")
    print(f"{c_lower} lower letters")
    print(f"{p_marks} punctuation marks")
    print(f"{name.count(' ')} spaces")
    print(f"{c_digit} digits")


def main():
    if len(sys.argv) != 2:
        print("What is the text to count?")
        name = "Hello World!"
        print(name)
        building(name)
    else:
        building(sys.argv[1])


if __name__ == "__main__":
    main()
