def aptitude_test():
    print("\nStage 1: Aptitude Test")
    score = int(input("Enter your aptitude test score (out of 100): "))
    if score >= 60:
        print("Congratulations! You passed the aptitude test.")
        return True
    else:
        print("Sorry, you did not pass the aptitude test.")
        return False
def technical_round():
    print("\nStage 2: Technical Interview")
    questions = [
        "Explain the OOP principles.",
        "What is a database schema?",
        "Write a Python program to reverse a string.",
        "What is the difference between TCP and UDP?",