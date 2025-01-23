import random
from bodyworkout import compute_caloric_needs, generate_workout_plan

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

def get_input(prompt):
    """
    Utility function to get input from the user and allow for escape.
    """
    user_input = input(prompt).strip()
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the application. Have a great day!")
        exit()
    return user_input

def main():
    print("Hello, welcome to Rick Kabuto's Body Workout Generator. Please Hit Enter to continue")
    get_input("")

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
        body_type_choice = get_input("Enter your body type (1 for Ectomorph, 2 for Mesomorph, 3 for Endomorph): ")
        if body_type_choice in body_type_mapping:
            body_type = body_type_mapping[body_type_choice]
            break
        else:
            print("Not a valid input. Please enter 1, 2, or 3.")

    weight = float(get_input("Enter your weight in pounds: "))
    months = int(get_input("Enter the number of months you want to gain 10-15 pounds of muscle: "))

    try:
        workout_list = load_workouts("Workout_List.txt")
    except FileNotFoundError:
        print("Error: Workout list file not found.")
        return

    schedule = generate_workout_plan(body_type, weight, months, workout_list)
    print(schedule)

if __name__ == "__main__":
    main()
