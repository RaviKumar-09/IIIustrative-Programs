def aptitude_test():
    print("\nStage 1: Aptitude Test")
    score = int(input("Enter your aptitude test score (out of 100): "))
    if score >= 60:
        print("Congratulations! You passed the aptitude test.")
        return True