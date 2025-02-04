# Function to check if the student can attend class

def can_attend_class(total_classes, attended_classes, min_attendance=75):
    attendance_percentage = (attended_classes / total_classes) * 100

    print(f"Attendance Percentage: {attendance_percentage:.2f}%")

    if attendance_percentage >= min_attendance:
        return "Yes, you can attend the class. 😊"
    else:
        return "No, you are not allowed to attend the class. 😞"
    
    # Taking user input
total_classes = int(input("Enter the total number of classes: "))
attended_classes = int(input("Enter the number of classes you attended: "))
# Checking attendance
result = can_attend_class(total_classes, attended_classes)