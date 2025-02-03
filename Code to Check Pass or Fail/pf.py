# Function to check pass or fail

def check_pass_fail(marks, passing_marks=35):
    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"
# Take user input
marks = float(input("Enter your marks: "))

# Check result
result = check_pass_fail(marks)