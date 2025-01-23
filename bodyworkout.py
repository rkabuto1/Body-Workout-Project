import random

def compute_caloric_needs(body_type, weight, months):
    """
    Generate the caloric needs formula based on body type, weight, and muscle growth goals.
    """

    body_type_multiplier = {
        "ectomorph": 20,  
        "mesomorph": 18,
        "endomorph": 16   
    }

    base_calories = weight * body_type_multiplier[body_type]
    surplus_calories = 500
    total_calories = base_calories + surplus_calories

    protein_min = weight * 1.0
    protein_max = weight * 1.2

    return f"""
To gain 10-15 pounds of muscle in {months} months:
1. Calculate your base calorie needs: {weight} (lbs) x {body_type_multiplier[body_type]} = {base_calories} calories/day.
2. Add a surplus of approximately 500 calories/day for muscle growth.
3. Total Daily Calorie Intake: {total_calories} calories/day.
4. Aim for a protein intake of {protein_min:.1f}–{protein_max:.1f} grams per day.
"""

def generate_workout_plan(body_type, weight, months, workout_list):
    caloric_needs = compute_caloric_needs(body_type, weight, months)

    body_type_workouts = {
        "ectomorph": {"sets": 3, "reps": "8-10"},
        "mesomorph": {"sets": 4, "reps": "10-12"},
        "endomorph": {"sets": 5, "reps": "12-15"}
    }

    schedule = {"Push": [], "Pull": [], "Legs": []}

    chest_exercises = random.sample(workout_list["Chest"], min(3, len(workout_list["Chest"])))
    shoulder_exercises = random.sample(workout_list["Shoulders"], min(1, len(workout_list["Shoulders"])))
    tricep_exercises = random.sample(workout_list["Tricep"], min(2, len(workout_list["Tricep"])))
    schedule["Push"] = chest_exercises + shoulder_exercises + tricep_exercises

    back_exercises = random.sample(workout_list["Back"], min(4, len(workout_list["Back"])))
    bicep_exercises = random.sample(workout_list["Bicep"], min(2, len(workout_list["Bicep"])))
    schedule["Pull"] = back_exercises + bicep_exercises

    leg_exercises = random.sample(workout_list["Legs"], min(4, len(workout_list["Legs"])))
    schedule["Legs"] = leg_exercises

    sets = body_type_workouts[body_type]["sets"]
    reps = body_type_workouts[body_type]["reps"]

    formatted_schedule = f"{caloric_needs}\n{body_type.capitalize()} Push Pull Legs Schedule:\n"
    for day, exercises in zip(["Push (Mon/Thu)", "Pull (Tue/Fri)", "Legs (Wed/Sat)"], schedule.values()):
        formatted_schedule += f"\n{day}:\n"
        for exercise in exercises:
            formatted_schedule += f"  - {exercise} ({sets} sets of {reps} reps)\n"
    formatted_schedule += "\nSunday: Rest or Active Recovery"
    
    return formatted_schedule
