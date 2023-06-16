import argparse
from utils.print_color import print_colored


def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines


def group_lines_with_at_symbol(lines):
    line_groups = {}
    current_group = []
    last_register = None

    for line in lines:
        if line.startswith("@"):
            current_group.append(line)
            last_register = line
        elif current_group:
            if len(current_group) > 1:
                current_group = current_group[:-1]
            line_groups[last_register] = current_group
            current_group = []
            last_register = None

    return line_groups


def check_alphabetical_order(group):
    return group == sorted(group)


def check_line_groups_order(line_groups):
    registers = list(line_groups.values())
    sorted_registers = sorted(registers)

    if registers == sorted_registers:
        return True
    else:
        first_unordered_register = next(
            x for x, y in zip(registers, sorted_registers) if x != y
        )

        print_colored(
            f"❌ Scenario: {first_unordered_register} is unordered.", color="red"
        )

        # Find the index where the order is incorrect
        index = registers.index(first_unordered_register)

        # Get the correct order of registers
        correct_order = sorted_registers[index:]

        print("Correct order (from the wrong record):")
        for register in correct_order:
            print(register)

        return False


if __name__ == "__main__":
    # Remember to run with parameter FEATURE_FILE:
    # python run_check_behave_order.py br_worker_leave_change_v1

    parser = argparse.ArgumentParser()
    parser.add_argument("FEATURE_FILE", help="Path to the feature file")
    args = parser.parse_args()
    file = args.FEATURE_FILE

    behave_adp = "C:/Users/fabio.picoli/projects/adp/automation/ala.marketplace"
    filename = f"{behave_adp}/marketplace/features/{file}.feature"
    message_ok = True

    # Read the file and obtain lines
    lines = read_file(filename)

    # Group the lines starting with "@" symbol and convert into a dictionary
    groups = group_lines_with_at_symbol(lines)
    # remove one register groups, like @periodo, @especificos e etc.
    groups_filtered = dict(filter(lambda item: len(item[1]) > 1, groups.items()))

    for last_register, group in groups_filtered.items():
        if not check_alphabetical_order(group):
            message_ok = False
            print_colored(
                f"❌ Scenario: {last_register} has TAGS unordered.", color="red"
            )

    if not check_line_groups_order(groups_filtered):
        message_ok = False

    if message_ok:
        print_colored("✔ No ordering errors were found.\n", color="green")
