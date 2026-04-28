import json
import os

def doctor():
    file_path = "entry.json"

    # Simple login simulation: Ask which doctor is logging in
    # This ensures you only see YOUR schedule
    doc_name = input("\nEnter your name to access your dashboard: ")

    while True:
        print(f"\n╔{"═" * 35}╗")
        print(f"║ Dr. {doc_name[:28]:<28}  ║")  # Limits name length for UI
        print(f"╠{"═" * 35}╣")
        print(f"║ [1] View Daily Schedule           ║")
        print(f"║ [2] Record Consultation (Notes)   ║")
        print(f"║ [3] Update Appointment Status     ║")
        print(f"║ [4] Back to Main Menu             ║")
        print(f"╚{"═" * 35}╝")

        try:
            choice = int(input("Select an option: "))

            if choice == 1:
                display_schedule(doc_name, file_path)
            elif choice == 2:
                record_clinical_notes(doc_name, file_path)
            elif choice == 3:
                update_appt_status(doc_name, file_path)
            elif choice == 4:
                print("Returning to main menu...")
                break
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a number (1-4).")


# --- Helper Functions for the Doctor ---

def display_schedule(doc_name, file_path):
    if not os.path.exists(file_path):
        print("No records found.")
        return

    with open(file_path, "r") as f:
        data_list = json.load(f)

    print(f"\n--- Schedule for Dr. {doc_name} ---")
    print(f"{'ID':<4} | {'Patient':<15} | {'Time':<10} | {'Status':<12}")
    print("-" * 50)

    found = False
    for i, item in enumerate(data_list):
        # We look for entries of type 'appointment' belonging to this doctor
        if item.get("type") == "appointment" and item.get("doctor_name").lower() == doc_name.lower():
            print(f"{i:<4} | {item.get('patient_name'):<15} | {item.get('time'):<10} | {item.get('status'):<12}")
            found = True

    if not found:
        print("No appointments found for you today.")


def record_clinical_notes(doc_name, file_path):
    if not os.path.exists(file_path): return

    with open(file_path, "r") as f:
        data_list = json.load(f)

    try:
        idx = int(input("\nEnter Appointment ID to record consultation: "))
        if 0 <= idx < len(data_list) and data_list[idx].get("doctor_name").lower() == doc_name.lower():

            print(f"Consulting: {data_list[idx]['patient_name']}")
            data_list[idx]["diagnosis"] = input("Enter Diagnosis: ")
            data_list[idx]["treatment"] = input("Prescribe Treatment: ")
            data_list[idx]["status"] = "Completed"

            with open(file_path, "w") as f:
                json.dump(data_list, f, indent=4)
            print("Consultation notes saved and status marked as 'Completed'.")
        else:
            print("Invalid ID or unauthorized access.")
    except (ValueError, IndexError):
        print("Invalid ID.")


def update_appt_status(doc_name, file_path):
    if not os.path.exists(file_path): return

    with open(file_path, "r") as f:
        data_list = json.load(f)

    try:
        idx = int(input("\nEnter Appointment ID to change status: "))
        if 0 <= idx < len(data_list) and data_list[idx].get("doctor_name").lower() == doc_name.lower():
            print("1. Completed | 2. Missed | 3. Cancelled")
            st_choice = input("Select Status (1-3): ")
            mapping = {"1": "Completed", "2": "Missed", "3": "Cancelled"}

            if st_choice in mapping:
                data_list[idx]["status"] = mapping[st_choice]
                with open(file_path, "w") as f:
                    json.dump(data_list, f, indent=4)
                print(f"Status updated to {mapping[st_choice]}.")
            else:
                print("Invalid selection.")
    except (ValueError, IndexError):
        print("Invalid ID.")

doctor()