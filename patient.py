class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=[]):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        self.__doctor = "None"
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms

    def full_name(self):
        """full name is first_name and surname"""
        return self.__first_name + " " + self.__surname

    def get_doctor(self):
        """returns the doctor"""
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor
        return self

    def print_symptoms(self):
        """prints all the symptoms"""
        for index, symptom in enumerate(self.__symptoms):
            print(f"{index+1:3}|{symptom}")

    def get_surname(self):
        """Returns the surname of the patient."""
        return self.__surname

    def get_postcode(self):
        """Returns the postcode of the patient."""
        return self.__postcode

    def get_illnesses(self):
        """Returns the list of symptoms/illnesses."""
        return self.__symptoms

    def to_dict(self):
        """Converts patient object to a dictionary."""
        return {
            "first_name": self.__first_name,
            "surname": self.__surname,
            "age": self.__age,
            "mobile": self.__mobile,
            "postcode": self.__postcode,
            "symptoms": self.__symptoms,
            "doctor": self.__doctor,
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a patient object from a dictionary."""
        return cls(
            data["first_name"],
            data["surname"],
            data["age"],
            data["mobile"],
            data["postcode"],
            data["symptoms"],
        ).link(data["doctor"])

    def __str__(self):
        return f"{self.full_name():^30}|{self.get_doctor():^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{self.__symptoms}"
