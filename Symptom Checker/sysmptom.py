def check_symptom(symptom):
      urgent_symptoms = ["shortness of breath", "chest pain", "high fever", "unconsciousness"]
      if symptom.lower() in urgent_symptoms:
        print("This symptom requires immediate medical attention!")