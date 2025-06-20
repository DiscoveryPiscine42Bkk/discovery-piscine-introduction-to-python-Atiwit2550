import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    input_str = sys.argv[1]
    z_found = False

    for char in input_str:
        if char == 'z':
            print('z', end='')
            z_found = True

    if not z_found:
        print("none")
    else:
        print()

if __name__ == "__main__":
    main()