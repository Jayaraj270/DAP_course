# Dictionary with student names and their marks
student_marks = {
    "Jay": 85,
    "Pree": 90,
    "Shalu": 78,
    "Gagan": 92
}

# input a student name
name = input("Enter the student's name: ")

# Check if the name exists in the dictionary
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"No record found for student named '{name}'.")
