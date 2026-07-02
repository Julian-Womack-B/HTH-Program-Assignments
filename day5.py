patients = [{"name":"John Doe", "age": 33, "temperature": 98.5}, {"name":"Jane Doe", "age": 29, "temperature": 99.1}, {"name": "The Rock", "age": 50, "temperature": 97.9}]
patients.append({"name": "Kevin Hart", "age": 41, "temperature": 98.7})
patients.append({"name": "Test Patient", "age": 40, "temperature": 99.0})
def check_patients(patients):
    for patient in patients:
        if patient["temperature"] > 99.0:
            print(f"Patient {patient["name"]} has a fever with a temperature of {patient["temperature"]}.")
        elif patient["temperature"] < 99.0:
            print(f"Patient {patient["name"]} has a temperature of {patient["temperature"]}, no fever detected.")
        else: 
            print(f"Monitor Patient: {patient["name"]}, temperature is {patient["temperature"]}.")
check_patients(patients)

def find_patient(name):
    found = False
    for patient in patients:
        if patient["name"] == name:
            print(f"{patient['name']}, Age: {patient['age']}, Temp: {patient['temperature']}")
            found = True
    if not found:
        print(f"Patient {name} not found.")
find_patient("lebron")

def update_temperature(name, new_temp):
    for patient in patients:
        if patient["name"] == name:
            print(f"Updated Patient Info: {patient["name"]}, age: {patient["age"]}, re-running temperature")
            patient["temperature"] = new_temp
            print(f"Updated {patient['name']}, Age: {patient['age']}, Temperature: {new_temp}")
update_temperature("Kevin Hart", 100.2)
check_patients(patients)


           
            
        