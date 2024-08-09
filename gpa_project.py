filename = "credit_gpa_calculator.txt"

try:
    with open(filename, "x") as file:
        file.write("This is a new file created as it didn't exist.")
        message = "File created successfully."
except FileExistsError:
    message = "File already exists."

def letter_grade_to_gpa(x):
    grade_to_gpa = {
        "AA": 4.0,
        "BA": 3.5,
        "BB": 3.0,
        "CB": 2.5,
        "CC": 2.0,
        "DC": 1.5,
        "DD": 1.0,
        "FF": 0.0
    }
    letter_grade = x.upper()
    gpa = grade_to_gpa.get(letter_grade, None)
    return gpa

action = input("Enter what to do: ")

if action.capitalize() == "Append":
    file = open(filename, "a")
    input_1 = input("Enter the course name: ")
    input_2 = input("Enter the letter grade: ")
    input_3 = int(input("Enter its ECTS value: "))
    input_4 = input("Enter type of course: ")
    line_to_write = f"{input_1} {input_2} {input_3} {input_4}\n"
    file.write(line_to_write)
    file.close()
else:
    import pandas as pd
    df = pd.read_csv(filename, sep=" ")

first_col = df["CourseCode"]
second_col = df["LetterGrade"]
third_col = df["Credits"]
fourth_col = df["Type"]

credit = 0;gpa = 0;field_elective = 0;free_elective = 0

for i in third_col:
    credit += i

for x in range(len(third_col)):
    points = second_col[x]
    out_of_four = letter_grade_to_gpa(points)
    cred = third_col[x]
    type = fourth_col[x]
    if type == "A":
        field_elective += cred
    elif type == "S":
        free_elective += cred
    proportion = cred/credit
    effect = out_of_four * proportion
    gpa += effect

print(credit,gpa,field_elective,free_elective)