#using functions to manage student results
def student_result(name, marks):
    total = 0

    for m in marks:
        total += m

    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return total, average, grade


# input section
student_name = input("Enter student name: ")
marks_list = []

for i in range(5):
    mark = int(input(f"Enter marks of subject {i+1}: "))
    marks_list.append(mark)

# function call
total, avg, grade = student_result(student_name, marks_list)

# output
print("\n--- Student Result ---")
print("Name:", student_name)
print("Total Marks:", total)
print("Average:", avg)
print("Grade:", grade)