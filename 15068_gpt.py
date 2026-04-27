def convert_units(conversion_line, m):
    # Parse the input
    parts = conversion_line.split()
    n = int(parts[0])
    names = parts[1::2]
    rates = list(map(int, parts[2::2]))

    # Calculate the amount in each unit using integer arithmetic
    amounts = [0] * n
    remaining = m

    for i in range(n-1, 0, -1):
        amounts[i] = remaining % rates[i-1]
        remaining = remaining // rates[i-1]

    amounts[0] = remaining

    # First output line: rounded to the nearest integer of the largest unit
    largest_unit_amount = amounts[0]
    if amounts[1] * 2 >= rates[0]:
        largest_unit_amount += 1
    print(f"{largest_unit_amount} {names[0]}")

    # Second output line: two largest units
    first_unit_amount = amounts[0]
    second_unit_amount = amounts[1]

    print(f"{first_unit_amount} {names[0]}, {second_unit_amount} {names[1]}")

# Example usage:
conversion_line = "4 days 24 hours 60 minutes 60 seconds"
m = 2000000
convert_units(conversion_line, m)


convert_units(input(), int(input()))
