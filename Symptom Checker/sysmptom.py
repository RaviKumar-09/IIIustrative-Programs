# check_symptom
def check_symptom(symptom):
      # urgent_symptom
      urgent_symptoms = ["shortness of breath", "chest pain", "high fever", "unconsciousness"]
      # symptom for lower
      if symptom.lower() in urgent_symptoms:
        # print Statement
        print("This symptom requires immediate medical attention!")
   # else:
        # print("Monitor your symptom. If it worsens, consult a doctor.")
# Example usage
# symptom
symptom = input("Enter a symptom: ")
check_symptom(symptom)