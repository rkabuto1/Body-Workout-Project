import random

def calculate_calorie_formula(body_type, weight, months):
    """
    Generate the calorie formula based on body type, weight, and muscle gain goals.
    """
    # General guidelines for calorie surplus
    body_type_multiplier = {
        "ectomorph": 20,  # Higher multiplier for faster metabolism
        "mesomorph": 18,  # Moderate multiplier
        "endomorph": 16   # Lower multiplier due to slower metabolism
    }

    # Approximate total calorie intake per day
    daily_calories = weight * body_type_multiplier[body_type]
    surplus_calories = 500  # Approximate surplus for muscle gain
    total_calories = daily_calories + surplus_calories

    return f"""
To gain 10-15 pounds of muscle in {months} months:
1. Calculate your base calorie needs: {weight} (lbs) x {body_type_multiplier[body_type]} = {daily_calories} calories/day.
2. Add a surplus of approximately 500 calories/day for muscle growth.
3. Total Daily Calorie Intake: {total_calories} calories/day.
4. Aim for a protein intake of 1–1.2g per pound of body weight.
"""

def generate_schedule(body_type, weight, months, workout_list):
    # Calorie formula at the top
    calorie_formula = calculate_calorie_formula(body_type, weight, months)

    body_type_sets = {
        "ectomorph": {"sets": 3, "reps": "8-10"},
        "mesomorph": {"sets": 4, "reps": "10-12"},
        "endomorph": {"sets": 5, "reps": "12-15"}
    }

    schedule = {"Push": [], "Pull": [], "Legs": []}

    # Distribute exercises for Push Day
    chest_exercises = random.sample(workout_list["Chest"], min(3, len(workout_list["Chest"])))
    shoulder_exercises = random.sample(workout_list["Shoulders"], min(1, len(workout_list["Shoulders"])))
    tricep_exercises = random.sample(workout_list["Tricep"], min(2, len(workout_list["Tricep"])))
    schedule["Push"] = chest_exercises + shoulder_exercises + tricep_exercises

    # Distribute exercises for Pull Day
    back_exercises = random.sample(workout_list["Back"], min(4, len(workout_list["Back"])))
    bicep_exercises = random.sample(workout_list["Bicep"], min(2, len(workout_list["Bicep"])))
    schedule["Pull"] = back_exercises + bicep_exercises

    # Distribute exercises for Leg Day
    leg_exercises = random.sample(workout_list["Legs"], min(4, len(workout_list["Legs"])))
    schedule["Legs"] = leg_exercises

    # Get sets and reps for the chosen body type
    sets = body_type_sets[body_type]["sets"]
    reps = body_type_sets[body_type]["reps"]

    # Format the schedule
    formatted_schedule = f"{calorie_formula}\n{body_type.capitalize()} Push Pull Legs Schedule:\n"
    for day, exercises in zip(["Push (Mon/Thu)", "Pull (Tue/Fri)", "Legs (Wed/Sat)"], schedule.values()):
        formatted_schedule += f"\n{day}:\n"
        for exercise in exercises:
            formatted_schedule += f"  - {exercise} ({sets} sets of {reps} reps)\n"
    formatted_schedule += "\nSunday: Rest or Active Recovery"
    
    return formatted_schedule

def load_workouts(file_name):
    workout_dict = {}
    category = None

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line.startswith("1.") and line != "" and not line[0].isdigit():
                category = line  
                workout_dict[category] = []
            elif line.startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.")):
                if category is None:
                    raise ValueError("Error: Workout found without a category. Check the file format.")
                workout = line.split(" ", 1)[1]
                workout_dict[category].append(workout)

    return workout_dict

def main():
    print("Hello, welcome to Rick Kabuto's Body Workout Generator. Please Hit Enter to continue")
    input()

    ectomorph_info = """
    1. Ectomorph:
       - Naturally lean with a fast metabolism, making it hard to gain weight or muscle.
       - Focus on heavy compound lifts and a calorie surplus with high protein to build muscle.
       - Ensure sufficient recovery time between workouts.
    """

    mesomorph_info = """
    2. Mesomorph:
       - Naturally athletic and muscular, with broad shoulders and a narrow waist.
       - Responds well to a balanced training routine combining strength and hypertrophy.
       - Diet can be flexible, adjusted for bulking, cutting, or maintenance goals.
    """

    endomorph_info = """
    3. Endomorph:
       - Tends to have a rounder physique and stores fat more easily, but gains muscle readily.
       - Focus on high-volume training and circuits to burn calories while building strength.
       - Maintain a calorie-controlled diet with high protein and incorporate regular cardio.
    """

    print(ectomorph_info)
    print(mesomorph_info)
    print(endomorph_info)

    body_type_mapping = {
        "1": "ectomorph",
        "2": "mesomorph",
        "3": "endomorph"
    }

    while True:
        body_type_choice = input("Enter your body type (1 for Ectomorph, 2 for Mesomorph, 3 for Endomorph): ").strip()
        if body_type_choice in body_type_mapping:
            body_type = body_type_mapping[body_type_choice]
            break
        else:
            print("Not a valid input. Please enter 1, 2, or 3.")

    weight = float(input("Enter your weight in pounds: ").strip())
    months = int(input("Enter the number of months you want to gain 10-15 pounds of muscle: ").strip())

    try:
        workout_list = load_workouts("Workout_List.txt")
    except FileNotFoundError:
        print("Error: Workout list file not found.")
        return

    schedule = generate_schedule(body_type, weight, months, workout_list)
    print(schedule)

if __name__ == "__main__":
    main()
