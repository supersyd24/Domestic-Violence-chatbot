import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
sadness = ctrl.Antecedent(np.arange(0, 11, 1), 'sadness')
frustration = ctrl.Antecedent(np.arange(0, 11, 1), 'frustration')
empathy_score = ctrl.Consequent(np.arange(0, 11, 1), 'empathy_score')

# Membership functions for sadness
sadness['low'] = fuzz.trimf(sadness.universe, [0, 0, 5])
sadness['moderate'] = fuzz.trimf(sadness.universe, [3, 5, 7])
sadness['high'] = fuzz.trimf(sadness.universe, [5, 10, 10])

# Membership functions for frustration
frustration['low'] = fuzz.trimf(frustration.universe, [0, 0, 5])
frustration['moderate'] = fuzz.trimf(frustration.universe, [3, 5, 7])
frustration['high'] = fuzz.trimf(frustration.universe, [5, 10, 10])

# Membership functions for empathy_score
empathy_score['low'] = fuzz.trimf(empathy_score.universe, [0, 0, 5])
empathy_score['moderate'] = fuzz.trimf(empathy_score.universe, [3, 5, 7])
empathy_score['high'] = fuzz.trimf(empathy_score.universe, [5, 10, 10])
empathy_score['very_high'] = fuzz.trimf(empathy_score.universe, [7, 10, 10])

# Define fuzzy rules
rule1 = ctrl.Rule(sadness['high'] & frustration['low'], empathy_score['high'])
rule2 = ctrl.Rule(sadness['moderate'] & frustration['moderate'], empathy_score['moderate'])
rule3 = ctrl.Rule(sadness['low'] & frustration['high'], empathy_score['moderate'])
rule4 = ctrl.Rule(sadness['high'] & frustration['high'], empathy_score['very_high'])

# Create control system and simulation
empathy_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
empathy_sim = ctrl.ControlSystemSimulation(empathy_ctrl)

# Simulate an example case
def get_empathy_response(sadness_level, frustration_level):
    empathy_sim.input['sadness'] = sadness_level
    empathy_sim.input['frustration'] = frustration_level
    
    # Compute the result
    empathy_sim.compute()
    score = empathy_sim.output['empathy_score']
    
    # Generate response based on empathy score
    if score >= 7:
        return f"Empathy Score: {score:.2f} - I understand how difficult this must be for you. Let’s work together to find a way forward."
    elif score >= 5:
        return f"Empathy Score: {score:.2f} - It seems like you're going through a tough time. I'm here to support you."
    else:
        return f"Empathy Score: {score:.2f} - I'm here to help. Tell me more about what you're feeling."

# Test the system with an example input
print(get_empathy_response(sadness_level=8, frustration_level=3))
print(get_empathy_response(sadness_level=5, frustration_level=5))


