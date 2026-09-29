def get_values():
    count = int(input("Enter count: "))
    values = []
    for _ in range(count):
        val = input()
        values.append(val)
    return values


def add_unique(value, unique_list, positions_list):
    if not value.strip():
        print("Empty value entered and skipped.")
        return False

    for item in unique_list:
        if item.lower() == value.lower():
            pos = positions_list[unique_list.index(item)]
            print(f"{value} -> duplicate value, first entered at position {pos}")
            return False

    unique_list.append(value)
    print(f"{value} -> new value, added to list")
    return True


def process_values(raw_values):
    unique_list = []
    positions_list = []
    duplicate_count = 0

    for idx, val in enumerate(raw_values, start=1):
        if add_unique(val, unique_list, positions_list):
            positions_list.append(idx)
        else:
            if val.strip():
                duplicate_count += 1

    return unique_list, positions_list, duplicate_count


def show_report(unique_list, positions_list, duplicate_count):
    print("\nFinal Report:")
    print(f"Unique values: {unique_list}")
    print(f"Duplicate count: {duplicate_count}")
    print(f"Unique count: {len(unique_list)}")
    print("\nFirst position entered:")
    for item, pos in zip(unique_list, positions_list):
        print(f"{item} -> {pos}")
        
if __name__ == "__main__":
   raw_vals = get_values()
   uniques, positions, duplicates = process_values(raw_vals)
   show_report(uniques, positions, duplicates)