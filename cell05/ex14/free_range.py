import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        numbers = list(range(start, end + 1)) if start <= end else list(range(start, end - 1, -1))
        print(numbers)
    except ValueError:
        print("none")

if __name__ == "__main__":
    main()