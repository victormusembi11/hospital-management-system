import tkinter as tk
from tkinter import simpledialog, messagebox

from doctor import Doctor
from patient import Patient


class HospitalManagementSystemUI:
    def __init__(self, master, doctors, patients, discharged_patients):
        self.doctors = doctors
        self.patients = patients
        self.discharged_patients = discharged_patients
        self.master = master
        self.master.title("Hospital Management System")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(
            self.master,
            text="Welcome to Hospital Management System",
            font=("Helvetica", 16),
        ).pack(pady=10)

        login_button = tk.Button(self.master, text="Login", command=self.login)
        login_button.pack(pady=10)

    def login(self):
        username = simpledialog.askstring("Login", "Enter your username:")
        password = simpledialog.askstring("Login", "Enter your password:")

        if username == "admin" and password == "123":
            self.show_menu()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    def show_menu(self):
        menu_window = tk.Toplevel(self.master)
        menu_window.title("Hospital Management System - Menu")

        options = [
            "Register/view/update/delete doctor",
            "Discharge patients",
            "View discharged patient",
            "Assign doctor to a patient",
            "Update admin details",
            "Quit",
        ]

        for i, option in enumerate(options, start=1):
            tk.Button(
                menu_window,
                text=f"{i}. {option}",
                command=lambda o=option: self.handle_option(o),
            ).pack(pady=5)

    def handle_option(self, option):
        if option == "Register/view/update/delete doctor":
            self.register_view_update_doctor()
        elif option == "Discharge patients":
            self.discharge_patients()
        elif option == "View discharged patient":
            self.view_discharged_patients()
        elif option == "Assign doctor to a patient":
            self.assign_doctor_to_patient()
        elif option == "Update admin details":
            self.update_admin_details()
        elif option == "Quit":
            self.master.destroy()

    def register_view_update_doctor(self):
        doctor_window = tk.Toplevel(self.master)
        doctor_window.title("Doctor Management")

        tk.Label(doctor_window, text="Choose the operation:").pack(pady=10)

        operations = [
            "Register Doctor",
            "View Doctors",
            "Update Doctor",
            "Delete Doctor",
        ]

        for i, operation in enumerate(operations, start=1):
            tk.Button(
                doctor_window,
                text=f"{i}. {operation}",
                command=lambda op=operation: self.handle_doctor_operation(op),
            ).pack(pady=5)

        tk.Button(doctor_window, text="Back", command=doctor_window.destroy).pack(
            pady=5
        )

    def handle_doctor_operation(self, operation):
        if operation == "Register Doctor":
            self.register_doctor(self.doctors)
        elif operation == "View Doctors":
            self.view_doctors()
        elif operation == "Update Doctor":
            self.update_doctor()
        elif operation == "Delete Doctor":
            self.delete_doctor()

    def register_doctor(self, doctors):
        register_window = tk.Toplevel(self.master)
        register_window.title("Register Doctor")

        tk.Label(register_window, text="Enter the doctor's details:").pack(pady=10)

        first_name = tk.StringVar()
        surname = tk.StringVar()
        speciality = tk.StringVar()

        tk.Label(register_window, text="First Name:").pack()
        tk.Entry(register_window, textvariable=first_name).pack()

        tk.Label(register_window, text="Surname:").pack()
        tk.Entry(register_window, textvariable=surname).pack()

        tk.Label(register_window, text="Speciality:").pack()
        tk.Entry(register_window, textvariable=speciality).pack()

        tk.Button(
            register_window,
            text="Register",
            command=lambda: self.register_doctor_submit(
                first_name, surname, speciality
            ),
        ).pack(pady=5)

        tk.Button(register_window, text="Back", command=register_window.destroy).pack(
            pady=5
        )

    def register_doctor_submit(self, first_name, surname, speciality):
        if first_name.get() == "" or surname.get() == "" or speciality.get() == "":
            messagebox.showerror("Error", "Please fill all the fields.")
        else:
            doctor = Doctor(first_name.get(), surname.get(), speciality.get())
            self.doctors.append(doctor)
            messagebox.showinfo("Success", "Doctor registered.")
            first_name.set("")
            surname.set("")
            speciality.set("")
            self.view_doctors(self.doctors)

    def view_doctors(self):
        view_window = tk.Toplevel(self.master)
        view_window.title("View Doctors")

        tk.Label(view_window, text="List of Doctors").pack(pady=10)

        tk.Label(
            view_window, text="ID |          Full name           |  Speciality"
        ).pack()

        for i, doctor in enumerate(self.doctors, start=1):
            tk.Label(view_window, text=f"{i:2} | {doctor}").pack()

        tk.Button(view_window, text="Back", command=view_window.destroy).pack(pady=5)

    def update_doctor(self):
        update_window = tk.Toplevel(self.master)
        update_window.title("Update Doctor")

        tk.Label(update_window, text="List of Doctors").pack(pady=10)

        tk.Label(
            update_window, text="ID |          Full name           |  Speciality"
        ).pack()

        for i, doctor in enumerate(self.doctors, start=1):
            tk.Label(update_window, text=f"{i:2} | {doctor}").pack()

        tk.Label(update_window, text="Enter the ID of the doctor:").pack()
        doctor_id = tk.IntVar()
        tk.Entry(update_window, textvariable=doctor_id).pack()

        tk.Label(update_window, text="Choose the field to be updated:").pack()

        options = [1, 2, 3]  # Use integers instead of strings

        for i, option in enumerate(options, start=1):
            tk.Radiobutton(
                update_window,
                text=f"{i}. {'First name' if option == 1 else 'Surname' if option == 2 else 'Speciality'}",
                variable=doctor_id,  # Use doctor_id as the variable
                value=option,
            ).pack()

        tk.Button(
            update_window,
            text="Update",
            command=lambda: self.update_doctor_submit(
                doctor_id, options, update_window
            ),
        ).pack(pady=5)

        tk.Button(update_window, text="Back", command=update_window.destroy).pack(
            pady=5
        )

    def update_doctor_submit(self, doctor_id, options, update_window):
        if doctor_id.get() == "":
            messagebox.showerror("Error", "Please fill all the fields.")
        else:
            doctor_index = doctor_id.get() - 1
            if doctor_index < 0 or doctor_index > len(self.doctors) - 1:
                messagebox.showerror("Error", "Doctor not found.")
            else:
                doctor = self.doctors[doctor_index]
                selected_option = options.index(doctor_id.get()) + 1
                if selected_option == 1:
                    new_first_name = simpledialog.askstring(
                        "Update First Name", "Enter the new first name:"
                    )
                    doctor.set___first_name(new_first_name)
                elif selected_option == 2:
                    new_surname = simpledialog.askstring(
                        "Update Surname", "Enter the new surname:"
                    )
                    doctor.set___surname(new_surname)
                elif selected_option == 3:
                    new_speciality = simpledialog.askstring(
                        "Update Speciality", "Enter the new speciality:"
                    )
                    doctor.set_speciality(new_speciality)
                messagebox.showinfo("Success", "Doctor updated.")
                update_window.destroy()
                self.view_doctors()

    def delete_doctor(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Doctor")

        tk.Label(delete_window, text="List of Doctors").pack(pady=10)

        tk.Label(
            delete_window, text="ID |          Full name           |  Speciality"
        ).pack()

        for i, doctor in enumerate(self.doctors, start=1):
            tk.Label(delete_window, text=f"{i:2} | {doctor}").pack()

        tk.Label(delete_window, text="Enter the ID of the doctor:").pack()
        doctor_id = tk.IntVar()
        tk.Entry(delete_window, textvariable=doctor_id).pack()

        tk.Button(
            delete_window,
            text="Delete",
            command=lambda: self.delete_doctor_submit(
                doctor_id, delete_window  # Correct the method name here
            ),
        ).pack(pady=5)

        tk.Button(delete_window, text="Back", command=delete_window.destroy).pack(
            pady=5
        )

    def delete_doctor_submit(self, doctor_id, delete_window):
        if doctor_id.get() == "":
            messagebox.showerror("Error", "Please fill all the fields.")
        else:
            doctor_index = doctor_id.get() - 1
            if doctor_index < 0 or doctor_index > len(self.doctors) - 1:
                messagebox.showerror("Error", "Doctor not found.")
            else:
                remaining_doctors = [
                    doctor for i, doctor in enumerate(self.doctors) if i != doctor_index
                ]
                self.doctors.clear()
                self.doctors.extend(remaining_doctors)
                messagebox.showinfo("Success", "Doctor deleted.")
                delete_window.destroy()
                self.view_doctors()

    def discharge_patients(self):
        discharge_window = tk.Toplevel(self.master)
        discharge_window.title("Discharge Patients")

        tk.Label(discharge_window, text="List of Active Patients").pack(pady=10)

        tk.Label(
            discharge_window,
            text="ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode",
        ).pack()

        for i, patient in enumerate(patients, start=1):
            tk.Label(discharge_window, text=f"{i:2} | {patient}").pack()

        tk.Label(
            discharge_window, text="Enter the ID of the patient to discharge:"
        ).pack()
        patient_id = tk.IntVar()
        tk.Entry(discharge_window, textvariable=patient_id).pack()

        tk.Button(
            discharge_window,
            text="Discharge",
            command=lambda: self.discharge_patient_submit(patient_id, discharge_window),
        ).pack(pady=5)

        tk.Button(discharge_window, text="Back", command=discharge_window.destroy).pack(
            pady=5
        )

    def view_patients(self):
        view_window = tk.Toplevel(self.master)
        view_window.title("View Patients")

        tk.Label(view_window, text="List of Patients").pack(pady=10)

        tk.Label(
            view_window,
            text="ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode",
        ).pack()

        for i, patient in enumerate(self.patients, start=1):
            tk.Label(view_window, text=f"{i:2} | {patient}").pack()

        tk.Button(view_window, text="Back", command=view_window.destroy).pack(pady=5)

    def discharge_patient_submit(self, patient_id, discharge_window):
        if patient_id.get() == "":
            messagebox.showerror("Error", "Please fill all the fields.")
        else:
            patient_index = patient_id.get() - 1
            if patient_index < 0 or patient_index > len(patients) - 1:
                messagebox.showerror("Error", "Patient not found.")
            else:
                self.discharged_patients.append(patients.pop(patient_index))
                messagebox.showinfo("Success", "Patient discharged.")
                discharge_window.destroy()
                self.view_patients()

    def view_discharged_patients(self):
        view_window = tk.Toplevel(self.master)
        view_window.title("View Discharged Patients")

        tk.Label(view_window, text="List of Discharged Patients").pack(pady=10)

        tk.Label(
            view_window,
            text="ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode",
        ).pack()

        for i, patient in enumerate(self.discharged_patients, start=1):
            tk.Label(view_window, text=f"{i:2} | {patient}").pack()

        tk.Button(view_window, text="Back", command=view_window.destroy).pack(pady=5)

    def assign_doctor_to_patient(self):
        # Implement the logic for this option
        pass

    def update_admin_details(self):
        # Implement the logic for this option
        pass


doctors = [
    Doctor("John", "Smith", "Internal Med."),
    Doctor("Jone", "Smith", "Pediatrics"),
    Doctor("Jone", "Carlos", "Cardiology"),
]

patients = [
    Patient(
        "Sara",
        "Smith",
        20,
        "07012345678",
        "B1 234",
        ["high blood pressure", "heart failure"],
    ),
    Patient("Mike", "Jones", 37, "07555551234", "L2 2AB", ["Coughing"]),
    Patient("Daivd", "Smith", 15, "07123456789", "C1 ABC", ["Fever"]),
]

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystemUI(root, doctors, patients, [])
    root.mainloop()
