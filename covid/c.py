# List of common COVID symptoms
covid_symptoms = ["fever", "cough", "tiredness", "loss of taste", "difficulty breathing"]

# User input symptoms
user_symptoms = input("Enter your symptoms (comma separated): ").lower().split(",")

# Check for COVID symptoms
matched_symptoms = [symptom.strip() for symptom in user_symptoms if symptom.strip() in covid_symptoms]

