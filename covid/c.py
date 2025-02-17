# List of common COVID symptoms
covid_symptoms = ["fever", "cough", "tiredness", "loss of taste", "difficulty breathing"]

# User input symptoms
user_symptoms = input("Enter your symptoms (comma separated): ").lower().split(",")

# Check for COVID symptoms
matched_symptoms = [symptom.strip() for symptom in user_symptoms if symptom.strip() in covid_symptoms]

# Decision based on symptoms
if len(matched_symptoms) >= 2:
    print("⚠️ You may be COVID Positive! 😷 Please take a test and consult a doctor.")
else:
    print("✅ You are likely COVID Negative! Stay safe and healthy. 😊")


