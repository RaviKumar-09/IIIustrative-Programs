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
    ]
    for question in questions:
        print(f"Question: {question}")
        input("Your Answer: ")  # Simulate answering questions
    feedback = input("Did the interviewer give positive feedback? (yes/no): ").lower()
    if feedback == "yes":
        print("Great! You passed the technical round.")
        return True
    else:
        print("Sorry, you did not pass the technical round.")
        return False
def hr_round():
    print("\nStage 3: HR Interview")
    questions = [
        "Tell me about yourself.",
        "Why do you want to work at Accenture?",
        "Where do you see yourself in 5 years?",
        "What are your salary expectations?",
    ]
    for question in questions:
        print(f"Question: {question}")
        input("Your Answer: ")  # Simulate answering questions
    feedback = input("Did the HR give positive feedback? (yes/no): ").lower()
    if feedback == "yes":
        print("Congratulations! You passed the HR round.")
        return True
    else:
        print("Sorry, you did not pass the HR round.")
        return False