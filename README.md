# Body-Workout-Project

Updated Project Will Be Pushed Soon.

This Project is Old as of Janurary 21st 2025.

## Purpose
This program, "Rick Kabuto's Body Workout Generator," is designed to create a customized Push-Pull-Legs workout schedule tailored to a user's body type. The program accounts for three body types: Ectomorph, Mesomorph, and Endomorph, each with specific sets and repetitions based on their fitness needs. The exercises are loaded from an external file (`Workout_List.txt`), and the program generates a schedule by randomly selecting exercises for each workout day.

## Features
- **Body Type Selection:** Users can select their body type using numeric options (1 for Ectomorph, 2 for Mesomorph, and 3 for Endomorph).
- **Custom Workout Schedule:** Generates a randomized Push-Pull-Legs workout schedule based on the selected body type.
- **Error Handling:** Prompts users to re-enter input if an invalid option is provided.
- **Randomized Exercise Selection:** Ensures variety in the workout schedule.

## How to Run the Program

### Prerequisites
1. Ensure you have Python 3 installed on your system.
2. Create a text file named `Workout_List.txt` in the same directory as the script. The file should include workout categories and exercises formatted similarly to the example below:

```
Chest
1. Bench Press
2. Incline Bench Press
...

Back
1. Pull-Ups
2. Deadlifts
...
```

### Steps to Run
1. Clone or copy the script into a Python file, e.g., `bodyworkout.py`.
2. Open a terminal and navigate to the directory containing `bodyworkout.py` and `Workout_List.txt`.
3. Run the program using:
   ```
   python3 bodyworkout.py
   ```
4. Follow the prompts:
   - Press Enter to start.
   - Review the descriptions of body types.
   - Enter your body type (1 for Ectomorph, 2 for Mesomorph, or 3 for Endomorph).
5. The program will display a workout schedule based on your selection.

### Example Output
```
Hello, welcome to Rick Kabuto's Body Workout Generator. Please Hit Enter to continue

1. Ectomorph:
   - Naturally lean with a fast metabolism, making it hard to gain weight or muscle.
   ...

Enter your body type (1 for Ectomorph, 2 for Mesomorph, 3 for Endomorph): 1

Ectomorph Push Pull Legs Schedule:

Push (Mon/Thu):
  - Bench Press (3 sets of 8-10 reps)
  - Incline Bench Press (3 sets of 8-10 reps)
  ...

Sunday: Rest or Active Recovery
```

## Notes
- Ensure the `Workout_List.txt` file is properly formatted to avoid errors.
- If the file is missing or incorrectly formatted, the program will display an error message.
- The workout schedule is randomized, so different runs may generate different schedules.

