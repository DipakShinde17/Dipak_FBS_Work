num_students = int(input("Enter number of students: "))

total_percentage = 0  

for i in range(num_students):
    print(f"\nEnter marks for Student {i+1}:")
    m1 = int(input("Enter 1st subject marks: "))
    m2 = int(input("Enter 2nd subject marks: "))
    m3 = int(input("Enter 3rd subject marks: "))
    m4 = int(input("Enter 4th subject marks: "))
    m5 = int(input("Enter 5th subject marks: "))
    
    total = m1 + m2 + m3 + m4 + m5
    percentage = (total / 500) * 100
    total_percentage += percentage
    
    print(f"Percentage of Student {i+1}: {percentage:.2f}%")

# Calculate and display average percentage
average_percentage = total_percentage / num_students
print(f"\nAverage Percentage of all students: {average_percentage}%")