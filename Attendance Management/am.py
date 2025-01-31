# Initialize an empty dictionary to store attendance records
attendance = {}

# List of students (you can add more students as needed)
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

#Function to mark attendance
def mark_attendance():
    print("\nMarking Attendance:")
    for student in students:
         # Ask for the attendance status (Present or Absent)
        status = input(f"Is {student} present? (yes/no): ").strip().lower()
        if status == 'yes':
            attendance[student] = "Present"
        else:
            attendance[student] = "Absent"
# Function to display attendance
def display_attendance():
    print("\nAttendance Records:")
    for student, status in attendance.items():
        print(f"{student}: {status}")


        