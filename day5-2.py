def welcome_message():
    print("Welcome to the program!")

    name = input("please enter your name: ")
    if name == "":
        print("Name cannot be empty. Please enter your name.")
    elif name:
        print(f"hello {name}, let us assist you today")
welcome_message()
def patient_info():
    print("Please enter your information below:")

    age = input("How old are you? ")
    while not age.isnumeric() or int(age) <=0:
        print("Please enter a valid age.")
        age = input("How old are you?")
    height = input("What is your height in inches? ")
    while not height.isnumeric() or int(height) <=0:
        print("Please enter a valid height.")
        height = input("What is your height in inches? ")
    weight = input("What is your weight in pounds?")
    while not weight.isnumeric() or int(weight) <=0:
        print("please enter a valid weight.")
        weight = input("What is your weight in pounds?" )
    gender = input("What is your gender? (M/F/PERSON/OTHER)") .upper()
    while gender not in ["M", "F", "Person", "Other"]:
        print("Please enter a valid input.")
        gender = input("What is your gender? (M/F/PERSON/OTHER")
    print(f"Thank you for providing your information. Here is a summary of your information: Age: {age}, Height: {height}, weight: {weight}, Gender: {gender}")
    answer = input("Is this information correct? (Y/N): ") .upper()
    if answer.lower() == "y":
        print("Thank you for confirming your information.")
        return
    else:
        print("Please re-enter your information.")
patient_info()
    
    
    
                        
    