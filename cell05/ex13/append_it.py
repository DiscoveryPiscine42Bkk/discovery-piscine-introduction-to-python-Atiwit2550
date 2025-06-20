import sys

def main():
    args = sys.argv[1:]

    if not args:
        print("none")
        return

    for word in args:
        if not word.endswith("ism"):
            print(word + "ism")

if __name__ == "__main__":
    main()