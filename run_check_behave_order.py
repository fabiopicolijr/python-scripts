from utils.print_color import print_colored

FEATURE_FILE = "br_worker_leave_request_return_v1.feature"


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

    if current_group:
        if len(current_group) > 1:
            current_group = current_group[:-1]
        line_groups[last_register] = current_group

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


behave_adp = "C:/Users/fabio.picoli/projects/adp/automation/ala.marketplace"
filename = f"{behave_adp}/marketplace/features/{FEATURE_FILE}"
message_ok = True

# Read the file and obtain lines
lines = read_file(filename)

# Group the lines starting with "@" symbol and convert into a dictionary
line_groups = group_lines_with_at_symbol(lines)

if not check_line_groups_order(line_groups):
    message_ok = False

for last_register, group in line_groups.items():
    if not check_alphabetical_order(group):
        message_ok = False
        print_colored(f"❌ Scenario: {last_register} has TAGS unordered.", color="red")

if message_ok:
    print_colored("✔ No ordering errors were found.\n", color="green")
