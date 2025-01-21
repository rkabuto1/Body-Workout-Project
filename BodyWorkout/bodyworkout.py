import random

def generate_schedule(body_type, workout_list):
    body_type_sets = {
        "ectomorph": {"sets": 3, "reps": "8-10"},
        "mesomorph": {"sets": 4, "reps": "10-12"},
        "endomorph": {"sets": 5, "reps": "12-15"}
    }

    schedule = {"Push": [], "Pull": [], "Legs": []}
    push_exercises = workout_list["Chest"] + workout_list["Shoulders"] + workout_list["Tricep"]
    pull_exercises = workout_list["Back"] + workout_list["Bicep"]
    leg_exercises = workout_list["Legs"]

    schedule["Push"] = random.sample(push_exercises, 6)
    schedule["Pull"] = random.sample(pull_exercises, 6)
    schedule["Legs"] = random.sample(leg_exercises, 6)

    sets = body_type_sets[body_type]["sets"]
    reps = body_type_sets[body_type]["reps"]

    formatted_schedule = f"\n{body_type.capitalize()} Push Pull Legs Schedule:\n"
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

    try:
        workout_list = load_workouts("Workout_List.txt")
    except FileNotFoundError:
        print("Error: Workout list file not found.")
        return

    schedule = generate_schedule(body_type, workout_list)
    print(schedule)

if __name__ == "__main__":
    main()