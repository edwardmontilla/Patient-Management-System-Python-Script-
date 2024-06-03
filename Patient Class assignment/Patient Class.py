#-----Patient Class-----        


# #Main
class Patient:
    def __init__(pat, id, name, disease, gender, age):
        pat.id = id
        pat.name = name
        pat.disease = disease
        pat.gender = gender
        pat.age = age

# #1 - Display patient list

def displayPatientsList():        
        pankaj = Patient(12, "Pankaj", "Cancer", "Male", 30)
        janina = Patient(13, "Janina", "Cold", "Female", 23)
        alona = Patient(14, "Alona", "Malaria", "Female", 45)
        ravi = Patient(15, "Ravi", "Diabetes", "Male", 65)

        print("ID\t", end=''), print("Name\t", end=''), print("Disease\t\t", end=''), print("Gender\t\t", end=''), print("Age")
        print(pankaj.id, end='\t'), print(pankaj.name, end='\t'), print(pankaj.disease, end='\t\t'), print(pankaj.gender, end='\t\t'), print(pankaj.age)
        print(janina.id, end='\t'), print(janina.name, end='\t'), print(janina.disease, end='\t\t'), print(janina.gender, end='\t\t'), print(janina.age)
        print(alona.id, end='\t'), print(alona.name, end='\t'), print(alona.disease, end='\t\t'), print(alona.gender, end='\t\t'), print(alona.age)
        print(ravi.id, end='\t'), print(ravi.name, end='\t'), print(ravi.disease, end='\t'), print(ravi.gender, end='\t\t'), print(ravi.age)
# displayPatientsList()


def readPatientsFile():
        f = open("patients.txt", "r")
        return f

# readfiles = readPatientsFile()
# print(readfiles.read())

def displayPatientsInfo():
        f = open("patients.txt", "r")

        print(f.readline().split("_"))
        print(f.readline().split("_"))
        print(f.readline().split("_"))
        print(f.readline().split("_"))
        print(f.readline().split("_"))
# displayPatientsInfo()

#2 - Search for patient by ID

def searchPatientById():
        readPatientsFile()
        searchId = input("Enter Patient id: \n")
        match = None
        for obj in searchId:
                if obj.id == searchId:
                        match = True
                        print("ID\t", end=''), print("Name\t", end=''), print("Disease\t\t", end=''), print("Gender\t\t", end=''), print("Age")
                        print(obj)
                        break
                else:
                        match = False

        if match == False:
                print("Can't find the Patient with the same id on the system")
# searchPatientById()

#3 - Add patient

def enterPatientinfo():
        patientId = input("Enter Patient id: \n")
        patientName = input("Enter Patient name: \n")
        patientDisease = input("Enter Patient disease: \n")
        patientGender = input("Enter Patient gender: \n")
        patientAge = int(input("Enter Patient age: \n"))

        newPatient = (patientId, patientName, patientDisease, patientGender, patientAge)
        return newPatient
# enterPatientinfo()

#4 - Edit patient info
def editPatientInfo():
        editPat = input("Please enter the id of the Patient that you want to edit their information: \n")
        match = None

        for obj in readPatientsFile:
                if obj == editPat:
                        match = True
                        obj.name = input("Enter new Name: \n")
                        obj.disease = input("Enter new disease: \n")
                        obj.gender = input("Enter new gender: \n")
                        obj.age = int(input("Enter new age: \n"))
                        Patient.formatPatientInfo()
                        Patient.addPatientToFile()
                        break
                else:
                        match = False

        if match == False:
                print("Can't find the patient with the same id on the system")
# editPatientInfo()

def formatPatientInfo():
        newText = Patient.enterPatientInfo()
        patText = "{}_{}_{}_{}_{}"
        modpatText = (patText.format(newText[0], newText[1], newText[2], newText[3], newText[4]))
        
        return modpatText

def addPatientToFile():
        modpatText = Patient.formatPatient.info()
        f = open("patients.txt", "a")

        f.write(modpatText)
        f.close()

        f = open("patients.txt")

        print(f.readlines)

def writeListOfPatientsToFile():
        pass



# -----Display Menu for Patient Class-----

print("Welcome to the Alberta Hostpital (AH) Management System \nSelect from the following options, or select 0 to stop:")
menu = int(input("1 - Doctors \n2 - Facilities \n3 - Laboratories \n4 - Patients \n"))

match menu:
        case 4:
                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))
                while True:
                        if patMenu == 1:
                                displayPatientsList()
                                print("Back to previous Menu")
                                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))

                        elif patMenu == 2:
                                searchPatientById()
                                print("Back to previous Menu")
                                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))

                        elif patMenu == 3:
                                enterPatientinfo()
                                print("Back to previous Menu")
                                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))

                        elif patMenu == 4:
                                editPatientInfo()
                                print("Back to previous Menu")
                                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))

                        elif patMenu == 5:
                                print("Back to previous Menu")
                                patMenu = int(input("\n Patients Menu: \n1 - Display patients list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu \n"))

                        else:
                                print("Invalid input")
                                break        



























# unused notes

# def formatPatientInfo(id, name, disease, gender, age):
#     patientInfo = {
#         "Id": id,
#         "Name": name,
#         "Disease": disease,
#         "Gender": gender,
#         "Age": age
#     }
#     return patientInfo
# patientData = addPatientToFile(1, "Skusta Clee", "Cold", "Male", "99")
# print(patientData)
        