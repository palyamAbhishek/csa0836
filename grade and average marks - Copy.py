num_subjects = int(input("Enter the number of subjects: "))
total_marks = 0

for i in range(num_subjects):
    marks = float(input("Enter marks for subject {}: ".format(i+1)))
    total_marks += marks

average_marks = total_marks / num_subjects
grade = 'A' if average_marks >= 90 else 'B' if average_marks >= 80 else 'C' if average_marks >= 70 else 'D' if average_marks >= 60 else 'F'

print("Average marks:", average_marks)
print("Grade:", grade)
