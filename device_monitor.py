def get_initial_readings():
    return [28, 31, 35, 37, 29]

def is_whole_number(text):
    if len(text) == 0:
        return False
    for index in range(len(text)):
        if text[index] not in "0123456789":
            return False
    return True

def add_reading(readings):
    text = input("Enter new reading: ")
    if len(text) == 0:
        print("\nInvalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("\nInvalid input. Enter a whole number only.")
    else:
        value = int(text)
        if value < 0 or value > 100:
            print("\nInvalid reading. Enter a value from 0 to 100.")
        else:
            readings.append(value)
            print("\nReading added successfully.")

def classify_reading(reading, warning_limit=30, critical_limit=35):
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"
    
def compute_total(readings):
    total = 0
    for reading in readings:
        total = total + reading
    return total

def compute_average(readings):
    if len(readings) == 0:
        return 0.0
    return compute_total(readings) / len(readings)

def find_minimum(readings):
    if len(readings) == 0:
        return None
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum

def find_maximum(readings):
    if len(readings) == 0:
        return None
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum

def count_category(readings, warning_limit, critical_limit, category):
    count = 0
    for reading in readings:
        cat = classify_reading(reading, warning_limit, critical_limit)
        if cat == category:
            count = count + 1
    return count

def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"

def display_readings(readings):
    print("CURRENT READINGS")
    print("----------------")
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")

def display_classifications(readings):
    print("READING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        print(f"{reading} °C -> {classify_reading(reading, 30, 35)}")

def display_summary(readings):
    num_readings = len(readings)
    total = compute_total(readings)
    avg = compute_average(readings)
    min_val = find_minimum(readings)
    max_val = find_maximum(readings)

    normal_count = count_category(readings, 30, 35, "NORMAL")
    warning_count = count_category(readings, 30, 35, "WARNING")
    critical_count = count_category(readings, 30, 35, "CRITICAL")

    normal_pct = (normal_count / num_readings) * 100 if num_readings > 0 else 0.0
    warning_pct = (warning_count / num_readings) * 100 if num_readings > 0 else 0.0
    critical_pct = (critical_count / num_readings) * 100 if num_readings > 0 else 0.0

    status = determine_overall_status(warning_count, critical_count)

    print("MONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {num_readings}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {avg:.2f} °C")
    print(f"Minimum temperature : {min_val} °C")
    print(f"Maximum temperature : {max_val} °C")
    print()
    print(f"NORMAL   : {normal_count} ({normal_pct:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_pct:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_pct:.2f}%)")
    print()
    print(f"Overall Status: {status}")

def display_menu():
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")
    print()

def main():
    readings = get_initial_readings()
    while True:
        display_menu()
        choice_text = input("Enter choice: ")
        if len(choice_text) == 0 or not is_whole_number(choice_text):
            print("\nInvalid choice. Please enter a number from 1 to 5.\n")
            continue

        choice = int(choice_text)
        if choice == 1:
            print()
            display_readings(readings)
            print()
        elif choice == 2:
            print()
            add_reading(readings)
            print()
        elif choice == 3:
            print()
            display_classifications(readings)
            print()
        elif choice == 4:
            print()
            display_summary(readings)
            print()
        elif choice == 5:
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.\n")

main()