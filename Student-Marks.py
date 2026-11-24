name = input("Enter Student Name: ")

marks = []

for i in range(5):
    m = float(input(f"Enter Subject {i+1} Marks: "))
    marks.append(m)

if any(m < 0 or m > 100 for m in marks):
    print("Invalid marks. Enter marks between 0 and 100.")
else:
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("\n----- RESULT -----")
    print("Student:", name)
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
