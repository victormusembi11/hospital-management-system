# Imports
from admin import Admin
from doctor import Doctor
from patient import Patient
import json


def save_patients_to_file(patients, file_path):
    """Saves patients' data to a file."""
    with open(file_path, "w") as file:
        json.dump([patient.to_dict() for patient in patients], file)


def load_patients_from_file(file_path):
    """Loads patients' data from a file."""
    patients = []
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            patients = [Patient.from_dict(patient_data) for patient_data in data]
    except FileNotFoundError:
        pass
    return patients


def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin("admin", "123", "B1 1AB")  # username is 'admin', password is '123'
    doctors = [
        Doctor("John", "Smith", "Internal Med."),
        Doctor("Jone", "Smith", "Pediatrics"),
        Doctor("Jone", "Carlos", "Cardiology"),
    ]
    patients = load_patients_from_file("patients.json")

    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True  # allow the program to run
            break
        else:
            print("Incorrect username or password.")

    while running:
        # print the menu
        print("Choose the operation:")
        print(" 1- Register/view/update/delete doctor")
        print(" 2- Discharge patients")
        print(" 3- View discharged patient")
        print(" 4- Assign doctor to a patient")
        print(" 5- Update admin detais")
        print(" 6- Quit")

        # get the option
        op = input("Option: ")

        if op == "1":
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)

        elif op == "2":
            # 2- View or discharge patients
            # ToDo2
            pass

            while True:
                op = input("Do you want to discharge a patient(Y/N):").lower()

                if op == "yes" or op == "y":
                    patients, discharged_patients = admin.discharge(
                        patients, discharged_patients
                    )

                elif op == "no" or op == "n":
                    break

                # unexpected entry
                else:
                    print("Please answer by yes or no.")

        elif op == "3":
            # 3 - view discharged patients
            admin.view_discharge(discharged_patients)

        elif op == "4":
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == "5":
            # 5- Update admin detais
            admin.update_details()

        elif op == "6":
            # 6 - Quit
            save_patients_to_file(patients, "patients.json")
            running = False

        else:
            # the user did not enter an option that exists in the menu
            print("Invalid option. Try again")


if __name__ == "__main__":
    main()
