# Function to check if the student can attend class

def can_attend_class(total_classes, attended_classes, min_attendance=75):
    attendance_percentage = (attended_classes / total_classes) * 100