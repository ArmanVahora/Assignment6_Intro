from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50

SCRIPT_DIR = Path(__file__).resolve().parent
FORLOOP_FILE = SCRIPT_DIR / "temperature_forloop.txt"
WHILELOOP_FILE = SCRIPT_DIR / "temperature_whileloop.txt"


def main():
    celsius = get_celsius()
    write_temperature_file_forloop(celsius)
    write_temperature_file_whileloop(celsius)


def get_celsius():
    # Get a valid Celsius temperature from the user
    while True:
        try:
            celsius = int(input("Enter Celsius (0-50): "))

            if MIN_CELSIUS <= celsius <= MAX_CELSIUS:
                return celsius
            else:
                print("Please enter a number between 0 and 50.")

        except ValueError:
            print("Please enter a whole number.")


def write_temperature_file_forloop(celsius):
    # Write the temperature table using a for-loop
    with open(FORLOOP_FILE, "w") as outfile:
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')
        outfile.write("------------------------------------\n")

        for degree in range(celsius + 1):
            fahrenheit = (degree * 1.8) + 32
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")


def write_temperature_file_whileloop(celsius):
    with open(WHILELOOP_FILE, "w") as outfile:
        outfile.write(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}\n')
        outfile.write("------------------------------------\n")
        degree = 0
        while degree <= celsius:
            # Calculate C to F
            fahrenheit = (degree * 1.8) + 32
            outfile.write(f"{degree:>8}\t\t{fahrenheit:>8.2f}\n")
            degree += 1


if __name__ == "__main__":
    main()