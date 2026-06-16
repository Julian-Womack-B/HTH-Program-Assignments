patients = ["Dana", "Eric", "Mia", "Jonas", "Priya"]
tempature = [98.6, 103.2, 99.1, 104.8, 97.1]

for i, temp in enumerate(tempature):
    print(f"{patients[i]}'s tempature is {tempature[i]}")

    if temp >104:
        print(f"{patients[i]} HAS A CRITICAL FEVER")
    elif temp >100.4:
        print(f"{patients[i]} has a Fever-monitor")
    elif temp >96.0:
        print(f"{patients[i]}'s tempature is normal")
    else:
        print(f"{patients[i]}'s IS HYPOTHEREMIC-WARM ASAP")
