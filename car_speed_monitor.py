
import csv
import os
from datetime import datetime

# ==========================================
# CAR SPEED MONITORING SYSTEM
# ==========================================

SPEED_LIMIT = 80
FILE_NAME = "car_speed_records.csv"

car_records = []


# ==========================================
# FUNCTION 1: DISPLAY WELCOME MESSAGE
# ==========================================

def welcome_message():

    print("=" * 55)
    print("       CAR SPEED MONITORING SYSTEM")
    print("=" * 55)

    print("Welcome to the Vehicle Speed Analysis Program")
    print("This program calculates and monitors car speeds.")

    print("=" * 55)


# ==========================================
# FUNCTION 2: CALCULATE SPEED
# ==========================================

def calculate_speed(distance, time):

    if time <= 0:
        print("Error: Time must be greater than zero.")
        return None

    speed = distance / time

    return round(speed, 2)


# ==========================================
# FUNCTION 3: CHECK SPEED LIMIT
# ==========================================

def check_speed_limit(speed):

    if speed < 0:
        return "INVALID SPEED"

    elif speed == 0:
        return "VEHICLE STOPPED"

    elif speed <= 40:
        return "LOW SPEED"

    elif speed <= SPEED_LIMIT:
        return "NORMAL SPEED"

    elif speed <= 100:
        return "OVERSPEEDING"

    elif speed <= 150:
        return "HIGH SPEED WARNING"

    else:
        return "EXTREME SPEED WARNING"


# ==========================================
# FUNCTION 4: CONVERT SPEED
# ==========================================

def convert_speed(speed):

    mph = speed * 0.621371

    meters_per_second = speed / 3.6

    print("\nSPEED CONVERSION")
    print("-" * 40)

    print(f"Speed in KM/H : {speed:.2f}")
    print(f"Speed in MPH  : {mph:.2f}")
    print(f"Speed in M/S  : {meters_per_second:.2f}")


# ==========================================
# FUNCTION 5: CALCULATE TRAVEL TIME
# ==========================================

def calculate_travel_time(distance, speed):

    if speed <= 0:
        print("Speed must be greater than zero.")
        return

    time = distance / speed

    hours = int(time)

    minutes = round((time - hours) * 60)

    if minutes == 60:
        hours += 1
        minutes = 0

    print("\nESTIMATED TRAVEL TIME")
    print("-" * 40)

    print(f"Distance : {distance} KM")
    print(f"Speed    : {speed} KM/H")

    print(f"Travel Time : {hours} hours {minutes} minutes")


# ==========================================
# FUNCTION 6: CALCULATE ACCELERATION
# ==========================================

def calculate_acceleration(initial_speed, final_speed, time):

    if time <= 0:
        print("Invalid time entered.")
        return

    # Convert KM/H into meters per second

    initial_velocity = initial_speed / 3.6

    final_velocity = final_speed / 3.6

    acceleration = (
        final_velocity - initial_velocity
    ) / time

    print("\nACCELERATION REPORT")
    print("-" * 40)

    print(f"Initial Speed : {initial_speed} KM/H")

    print(f"Final Speed   : {final_speed} KM/H")

    print(f"Time Taken    : {time} seconds")

    print(f"Acceleration  : {acceleration:.2f} m/s²")

    if acceleration > 0:
        print("Vehicle is accelerating.")

    elif acceleration < 0:
        print("Vehicle is decelerating.")

    else:
        print("Vehicle speed is constant.")


# ==========================================
# FUNCTION 7: ADD CAR RECORD
# ==========================================

def add_car_record():

    print("\nENTER CAR DETAILS")
    print("-" * 40)

    car_name = input("Enter Car Name: ")

    car_number = input("Enter Car Number: ")

    try:

        distance = float(
            input("Enter Distance Travelled (KM): ")
        )

        time = float(
            input("Enter Time Taken (Hours): ")
        )

        if distance < 0 or time <= 0:
            print("Invalid distance or time.")
            return

        speed = calculate_speed(distance, time)

        status = check_speed_limit(speed)

        current_date = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        record = {

            "Car Name": car_name,

            "Car Number": car_number,

            "Distance": distance,

            "Time": time,

            "Speed": speed,

            "Status": status,

            "Date": current_date

        }

        car_records.append(record)

        print("\nCAR SPEED RESULT")
        print("=" * 45)

        print(f"Car Name   : {car_name}")

        print(f"Car Number : {car_number}")

        print(f"Distance   : {distance} KM")

        print(f"Time       : {time} Hours")

        print(f"Speed      : {speed} KM/H")

        print(f"Status     : {status}")

        print("=" * 45)

        if speed > SPEED_LIMIT:

            excess_speed = speed - SPEED_LIMIT

            print("WARNING: SPEED LIMIT EXCEEDED!")

            print(f"Excess Speed: {excess_speed:.2f} KM/H")

    except ValueError:

        print("Please enter valid numerical values.")


# ==========================================
# FUNCTION 8: DISPLAY ALL CAR RECORDS
# ==========================================

def display_records():

    if len(car_records) == 0:

        print("\nNo car records available.")

        return

    print("\nALL CAR SPEED RECORDS")

    print("=" * 95)

    print(
        f"{'Car Name':<18}"
        f"{'Car Number':<18}"
        f"{'Distance':<12}"
        f"{'Time':<10}"
        f"{'Speed':<12}"
        f"{'Status':<20}"
    )

    print("-" * 95)

    for car in car_records:

        print(
            f"{car['Car Name']:<18}"
            f"{car['Car Number']:<18}"
            f"{car['Distance']:<12.2f}"
            f"{car['Time']:<10.2f}"
            f"{car['Speed']:<12.2f}"
            f"{car['Status']:<20}"
        )

    print("=" * 95)


# ==========================================
# FUNCTION 9: FIND FASTEST CAR
# ==========================================

def find_fastest_car():

    if not car_records:

        print("No records found.")

        return

    fastest_car = max(
        car_records,
        key=lambda car: car["Speed"]
    )

    print("\nFASTEST CAR REPORT")

    print("-" * 45)

    print(f"Car Name   : {fastest_car['Car Name']}")

    print(f"Car Number : {fastest_car['Car Number']}")

    print(f"Speed      : {fastest_car['Speed']} KM/H")

    print(f"Status     : {fastest_car['Status']}")


# ==========================================
# FUNCTION 10: FIND SLOWEST CAR
# ==========================================

def find_slowest_car():

    if not car_records:

        print("No records found.")

        return

    slowest_car = min(
        car_records,
        key=lambda car: car["Speed"]
    )

    print("\nSLOWEST CAR REPORT")

    print("-" * 45)

    print(f"Car Name   : {slowest_car['Car Name']}")

    print(f"Speed      : {slowest_car['Speed']} KM/H")


# ==========================================
# FUNCTION 11: CALCULATE AVERAGE SPEED
# ==========================================

def average_speed():

    if not car_records:

        print("No records available.")

        return

    total_distance = sum(
        car["Distance"] for car in car_records
    )

    total_time = sum(
        car["Time"] for car in car_records
    )

    average = total_distance / total_time

    print("\nAVERAGE SPEED REPORT")

    print("-" * 45)

    print(f"Total Distance : {total_distance:.2f} KM")

    print(f"Total Time     : {total_time:.2f} Hours")

    print(f"Average Speed  : {average:.2f} KM/H")


# ==========================================
# FUNCTION 12: OVERSPEEDING REPORT
# ==========================================

def overspeeding_report():

    overspeeding_cars = []

    for car in car_records:

        if car["Speed"] > SPEED_LIMIT:

            overspeeding_cars.append(car)

    print("\nOVERSPEEDING VEHICLE REPORT")

    print("=" * 50)

    if len(overspeeding_cars) == 0:

        print("No overspeeding vehicles detected.")

        return

    for car in overspeeding_cars:

        print(f"Car Name   : {car['Car Name']}")

        print(f"Car Number : {car['Car Number']}")

        print(f"Speed      : {car['Speed']} KM/H")

        print(f"Excess     : {car['Speed'] - SPEED_LIMIT:.2f} KM/H")

        print("-" * 50)

    print(
        f"Total Overspeeding Vehicles: "
        f"{len(overspeeding_cars)}"
    )


# ==========================================
# FUNCTION 13: SAVE RECORDS TO CSV
# ==========================================

def save_records():

    if not car_records:

        print("No records available to save.")

        return

    fieldnames = [

        "Car Name",

        "Car Number",

        "Distance",

        "Time",

        "Speed",

        "Status",

        "Date"

    ]

    try:

        with open(
            FILE_NAME,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            writer.writerows(car_records)

        print("\nRecords saved successfully!")

        print(f"File Name: {FILE_NAME}")

    except OSError as error:

        print(f"Unable to save records: {error}")


# ==========================================
# FUNCTION 14: LOAD PREVIOUS RECORDS
# ==========================================

def load_records():

    if not os.path.exists(FILE_NAME):

        return

    try:

        with open(
            FILE_NAME,
            mode="r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                row["Distance"] = float(row["Distance"])

                row["Time"] = float(row["Time"])

                row["Speed"] = float(row["Speed"])

                car_records.append(row)

        print("Previous records loaded successfully.")

    except (OSError, ValueError, KeyError) as error:

        print(f"Error loading records: {error}")


# ==========================================
# FUNCTION 15: SEARCH CAR
# ==========================================

def search_car():

    search_number = input(
        "\nEnter Car Number to Search: "
    )

    found = False

    for car in car_records:

        if car["Car Number"].lower() == search_number.lower():

            print("\nCAR FOUND")

            print("-" * 45)

            for key, value in car.items():

                print(f"{key}: {value}")

            found = True

    if not found:

        print("No matching car found.")


# ==========================================
# FUNCTION 16: DISPLAY MENU
# ==========================================

def display_menu():

    print("\n")
    print("=" * 55)

    print("           MAIN MENU")

    print("=" * 55)

    print("1. Add New Car Speed Record")

    print("2. Display All Car Records")

    print("3. Find Fastest Car")

    print("4. Find Slowest Car")

    print("5. Calculate Average Speed")

    print("6. Display Overspeeding Report")

    print("7. Convert Speed Units")

    print("8. Calculate Travel Time")

    print("9. Calculate Acceleration")

    print("10. Search Car by Number")

    print("11. Save Records to CSV")

    print("12. Exit Program")

    print("=" * 55)


# ==========================================
# FUNCTION 17: MAIN PROGRAM
# ==========================================

def main():

    welcome_message()

    load_records()

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice (1-12): "
        )

        if choice == "1":

            add_car_record()

        elif choice == "2":

            display_records()

        elif choice == "3":

            find_fastest_car()

        elif choice == "4":

            find_slowest_car()

        elif choice == "5":

            average_speed()

        elif choice == "6":

            overspeeding_report()

        elif choice == "7":

            try:

                speed = float(
                    input("Enter Speed in KM/H: ")
                )

                if speed < 0:
                    print("Speed cannot be negative.")
                else:
                    convert_speed(speed)

            except ValueError:

                print("Invalid speed entered.")

        elif choice == "8":

            try:

                distance = float(
                    input("Enter Distance in KM: ")
                )

                speed = float(
                    input("Enter Speed in KM/H: ")
                )

                if distance < 0:
                    print("Distance cannot be negative.")
                else:
                    calculate_travel_time(distance, speed)

            except ValueError:

                print("Invalid input.")

        elif choice == "9":

            try:

                initial = float(
                    input("Enter Initial Speed (KM/H): ")
                )

                final = float(
                    input("Enter Final Speed (KM/H): ")
                )

                time = float(
                    input("Enter Time Taken (Seconds): ")
                )

                if initial < 0 or final < 0:
                    print("Speed cannot be negative.")
                else:
                    calculate_acceleration(
                        initial,
                        final,
                        time
                    )

            except ValueError:

                print("Invalid numerical input.")

        elif choice == "10":

            search_car()

        elif choice == "11":

            save_records()

        elif choice == "12":

            save_records()

            print("\nThank you for using the system!")

            print("Drive safely!")

            break

        else:

            print("\nInvalid choice. Please try again.")


# ==========================================
# PROGRAM EXECUTION STARTS HERE
# ==========================================

if __name__ == "__main__":

    main()