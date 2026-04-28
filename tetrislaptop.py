import time
import json
import os

# ==========================================
#           ADMINISTRATOR MODULE
# ==========================================
class administrator_module:
    
    def administrator(self):
        administratorlist = [
            "Manage Doctors         ║",
            "Manage Clinic Schedule ║",
            "View Reports           ║",
            "Back                   ║"
        ]
        print(f"╔{"═" * 27 }╗\n║       Administrator       ║\n╠{"═" * 27 }╣")
        for i, list1 in enumerate(administratorlist, start=1):
            print(f"║[{i}] {list1}")
        print(f"╚{"═" * 27 }╝")

        try:
            user_input = int(input("Enter your choice: "))
            if user_input == 1:
                ad.manage_doctor()
            elif user_input == 2:
                ad.manage_clinic_schedule()
            elif user_input == 3:
                ad.viewreport()
            elif user_input == 4:
                print("Returning to main menu...")
                time.sleep(0.1)
                menu_choice()
            else:
                print("Please enter valid number!")
        except ValueError:
            print("Please enter only 1-4")

    file_path = "output.json"
    def manage_doctor(self):
        manage_doctor_list = [
                            "Add                    ║",
                            "View slot              ║",
                            "Update                 ║",
                            "Remove                 ║",
                            "Back                   ║",
                            ]
        print(f"╔{"═" * 27 }╗\n║       Manage Doctors      ║\n╠{"═" * 27 }╣")
        for i, list in enumerate(manage_doctor_list, start=1):
            print(f"║[{i}] {list}")
        print(f"╚{"═" * 27 }╝")

        try:
            choice_input = int(input("Enter choice: ")) #User input for manage_doctor
            if choice_input == 1: # Add
                print("\n╔═══════════════════════════════════════════╗")
                print("║             REGISTRATION FORM             ║")
                print("╠═══════════════════════════════════════════╣")
                print("║ Please enter the following details:       ║")
                print("╚═══════════════════════════════════════════╝")
                doctor_name = input("Doctor Name: ")
                specialization = input("Specialization: ")

                try: # float number for consultation fee
                    consultation_fee = float(input("Consultation Fee: "))
                    if consultation_fee < 0:
                        print("Error: Fee cannot be negative!")
                        return # Exit the function if input is invalid
                except ValueError:
                    print("Invalid input! Please enter numbers only (e.g. 150.50)")
                    return

                new_entry = {
                "doctor": doctor_name,
                "type": specialization,
                "fee": consultation_fee
                }

                file_path = "entry.json"
                data_list = []

                if os.path.exists(file_path):
                    try:
                        with open(file_path, "r") as f:
                            data_list = json.load(f) # Load existing data
                    except json.JSONDecodeError:
                        data_list = [] # Start fresh if file is empty/corrupt

                data_list.append(new_entry) # Add the new doctor to the list

                # 3. Write back to the file
                try:
                    with open(file_path, "w") as f:
                        json.dump(data_list, f, indent=4)
                    print(f"Data has been added to '{file_path}'")
                    ad.administrator()
                except IOError as e:
                    print(f"An error occurred: {e}")

    #""=========================================================================================="""
            elif choice_input == 2: # View Slot
                file_path = "entry.json"
                if os.path.exists(file_path):
                    with open(file_path, "r") as f:
                        data_list = json.load(f)

                    print("\n" + "="*75)
                    print(f"{'DOCTOR MANAGEMENT SYSTEM':^75}")
                    print("="*75)
                    # Header with fixed widths: ID(4), Name(20), Specialization(25), Fee(10)
                    print(f"{'ID':<4} | {'Name':<20} | {'Specialization':<25} | {'Fee (RM)':<10}")
                    print("-" * 75)

                    for i, doc in enumerate(data_list, start=1):
                        # Using .get() prevents crashing if a key is missing
                        name = doc.get("doctor", "N/A")
                        spec = doc.get("type", "N/A")
                        fee = doc.get("fee", 0.0)
                        print(f"{i:<4} | {name:<20} | {spec:<25} | {fee:<10.2f}")
                    print("="*75)
                else:
                    print("No doctor records found yet!")

            elif choice_input == 3: # Update
                file_path = "entry.json"
                if os.path.exists(file_path):
                    with open(file_path, "r") as f:
                        data_list = json.load(f)

                    target = input("Enter the EXACT name of the doctor to update: ")
                    found = False
                    for doc in data_list:
                        if doc["doctor"].lower() == target.lower():
                            print(f"Match found for {doc['doctor']}!")
                            doc["doctor"] = input("Enter New Name: ")
                            doc["type"] = input("Enter New Specialization: ")
                            doc["fee"] = float(input("Enter New Fee: "))
                            found = True
                            break

                    if found:
                        with open(file_path, "w") as f:
                            json.dump(data_list, f, indent=4)
                        print("Record updated successfully!")
                    else:
                        print("Doctor not found.")

            elif choice_input == 4: # Remove
                file_path = "entry.json"
                if os.path.exists(file_path):
                    with open(file_path, "r") as f:
                        data_list = json.load(f)

                    target = input("Enter name to remove: ")
                    # This creates a new list EXCLUDING the target name
                    new_list = [d for d in data_list if d["doctor"].lower() != target.lower()]

                    if len(new_list) < len(data_list):
                        with open(file_path, "w") as f:
                            json.dump(new_list, f, indent=4)
                        print("Record deleted!")
                    else:
                        print("Doctor not found.")

            elif choice_input == 5: # Back
                return # return without calling the function again

            else:
                print("Back to program")

        except ValueError:
            pass  # Add appropriate handling here

    def manage_clinic_schedule(self):
        file_path = "entry.json"

        # 1. Load existing data
        data_list = []
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                data_list = json.load(f)

        print("\n--- Manage Clinic Schedule ---")
        doc_target = input("Enter Doctor Name to set schedule: ")

        # Check if doctor exists first (Good Validation!)
        doctor_exists = any(d.get("doctor") == doc_target for d in data_list)

        if not doctor_exists:
            print("That doctor isn't registered yet!")
            return

        # 2. Collect Schedule Info
        slots_input = input("Enter available slots (separated by commas, e.g., 09:00, 10:00): ")
        slots_list = [s.strip() for s in slots_input.split(",")] # Clean up spaces

        try:
            max_appts = int(input("Set maximum appointments for the day: "))
        except ValueError:
            print("Invalid number!")
            return

        # 3. Create Schedule Entry
        new_schedule = {
            "type": "schedule",
            "doctor_name": doc_target,
            "time_slots": slots_list,
            "max_appts": max_appts
        }

        # Check if a schedule already exists for this doctor to avoid duplicates
        data_list = [item for item in data_list if not (item.get("type") == "schedule" and item.get("doctor_name") == doc_target)]

        data_list.append(new_schedule)

        # 4. Save back to JSON
        with open(file_path, "w") as f:
            json.dump(data_list, f, indent=4)

    def viewreport(self):

        file_path = "entry.json"
        try:
            with open(file_path, "r") as f:
                data_list = json.load(f)
                for doc in data_list:
                    if doc.get("type_category") == "doctor":
                        name = doc.get('doctor', 'Unknown')
                        fee = doc.get('fee', 0.0)
                        print(f"Doctor: {name} | Fee: RM{fee:.2f}")

        except FileNotFoundError:
            print("File not found!")
ad = administrator_module()

# ==========================================
#           RECEPTIONIST MODULE
# ==========================================
class receptionist:
    def receptionist():
        print("testign123")
        #START YOUR CODE HERE!!!
recept = receptionist()
# ==========================================
#           DOCTOR MODULE
# ==========================================

def doctor():
    print("tesing")
    #START YOUR CODE HERE!!!

# ==========================================
#           FINANCE MODULE
# ==========================================

def finance_officer():
    print("67676767")
    #START YOUR CODE HERE!!!

def menu_choice():
    choice = [
            "=============================================",
            " SmartClnic - Appointment & Patient System    ",
            "=============================================",
            "1. Administrator\n2. Receptionist\n3. Doctor\n4. Finance Officer\n5. Exit ",
            "============================================="
            ]

    while True:
        for selection in choice:
            print(selection)

        try:
            select = int(input("Enter your choice: "))
            if select == 1:
                print()
                ad.administrator()
            elif select == 2:
                recept.receptionist()
            elif select == 3:
                doctor()
            elif select == 4:
                finance_officer()
            elif select == 5:
                print("Exiting program....")
                break
            else:
                print("Please enter only 1-5")

        except ValueError:
            print("Enter a valid digit!")

if __name__ == "__main__":
    menu_choice()