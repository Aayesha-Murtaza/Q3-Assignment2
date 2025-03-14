student_record = [] # record list
# Data Input
continue_input =    "Y"
while(continue_input == "Y"):
    dict1 = {}
    dict1["name"] = input("Enter Student Name:")
    dict1["roll_no"] = input("Enter Roll Number:")
    dict1["maths"] = input("Enter Maths Marks:")
    dict1["physics"] = input("Enter Physics Marks:")
    dict1["urdu"] = input("Enter Urdu Marks:")
    dict1["english"] = input("Enter English Marks:")
    dict1["computer"] = input("Enter Computer Marks:")

    student_record.append(dict1)

    print("Do you want to enter another record?")
    continue_input = input("Enter Y/N: ")
    if continue_input != "N" and continue_input != "Y":
        while continue_input != "N" and continue_input != "Y":
            print("Invalid Input.")
            continue_input = input("Enter Y/N: ")
        
        

# Report Card Generation
for record in student_record:
    obtained_marks = 0
    for key,value in record.items():
        if key != "name" and key != "roll_no":
            obtained_marks += int(value)
    percentage = (obtained_marks / 500) * 100
    record["obtained_marks"] = obtained_marks
    record["percentage"] = percentage
    if percentage >= 80:
        record["grade"] = "A+"
    elif percentage >= 70:
        record["grade"] = "A"
    elif percentage >= 60:
        record["grade"] = "B"
    elif percentage >= 50:
        record["grade"] = "C"
    else:
        record["grade"] = "F"

# Report Card Display
for record in student_record:
    print("\nStudent Name: ", record["name"])
    print("Roll Number: ", record["roll_no"])
    print("Maths: ", record["maths"])
    print("Physics: ", record["physics"])
    print("Urdu: ", record["urdu"])
    print("English: ", record["english"])
    print("Computer: ", record["computer"])
    print("Obtained Marks: ", record["obtained_marks"])
    print("Percentage: ", record["percentage"])
    print("Grade: ", record["grade"])
    print("\n")
