
# How to run:
#   python change_calculator.py input.txt output.txt
#


import sys
import random

DIVISOR = 3  # could change


def calculate_change(owed_cents, paid_cents):
    if paid_cents <= owed_cents:
        return ""

    change = paid_cents - owed_cents

    denominations = [
        (100, "dollar"),
        (25,  "quarter"),
        (10,  "dime"),
        (5,   "nickel"),
        (1,   "penny")
    ]

    # If disivion by 3, shuffle coin order
    if owed_cents % DIVISOR == 0:
        random.shuffle(denominations)

    parts = []
    for value, name in denominations:
        count = change // value
        change %= value
        if count > 0:
            label = name if count == 1 else ("pennies" if name == "penny" else name + "s")
            parts.append(f"{count} {label}")

    return ", ".join(parts)


def process_file(input_path, output_path):
    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                outfile.write("\n")
                continue

            parts = line.split(",")
            if len(parts) != 2:
                outfile.write("\n")
                continue

            owed_cents = round(float(parts[0]) * 100)
            paid_cents = round(float(parts[1]) * 100)

            result = calculate_change(owed_cents, paid_cents)
            outfile.write(result + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python change_calculator.py <input_file> <output_file>")
        sys.exit(1)

    process_file(sys.argv[1], sys.argv[2])
    print("Done! Output written to", sys.argv[2])