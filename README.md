
# Rick Kabuto's Body Workout Generator

## Overview
Rick Kabuto's Body Workout Generator is a Python-based tool designed to create personalized workout schedules and nutritional guidance. It tailors a "Push-Pull-Legs" routine and calorie recommendations based on the user's body type, weight, and muscle gain goals.

## Features
1. **Personalized Calorie Formula**: Calculates the daily caloric intake required to gain 10-15 pounds of muscle in a specified number of months.
2. **Custom Workout Schedules**: Generates a weekly "Push-Pull-Legs" workout plan based on the user's body type and predefined exercise categories.
3. **Body Type Specifics**: Adapts workout intensity (sets and reps) for ectomorphs, mesomorphs, and endomorphs.
4. **Interactive Input**: Guides users through body type selection, weight input, and fitness goals.
5. **Dynamic Exercise Selection**: Randomly selects exercises for each workout day to ensure variety.

---

## How It Works

### 1. **Calorie Formula Calculation**
The tool calculates your daily caloric needs using the following formula:
- **Base Calorie Needs**: 
  - Ectomorph: `Weight (lbs) × 20`
  - Mesomorph: `Weight (lbs) × 18`
  - Endomorph: `Weight (lbs) × 16`
- **Add Calorie Surplus**: +500 calories/day to support muscle growth.

For example:
If you are an ectomorph weighing 150 lbs and want to gain muscle in 3 months:
```
Base Calories = 150 × 20 = 3000
Total Calories = 3000 + 500 = 3500 calories/day
```

### 2. **Workout Generation**
The workout schedule is based on a "Push-Pull-Legs" split:
- **Push Day (Chest, Shoulders, Triceps)**:
  - 3 Chest Exercises
  - 1 Shoulder Exercise
  - 2 Triceps Exercises
- **Pull Day (Back, Biceps)**:
  - 4 Back Exercises
  - 2 Biceps Exercises
- **Leg Day**:
  - 4 Leg Exercises

Each workout is formatted with appropriate sets and reps based on the user's body type:
- **Ectomorph**: 3 sets of 8-10 reps
- **Mesomorph**: 4 sets of 10-12 reps
- **Endomorph**: 5 sets of 12-15 reps

### 3. **Input File Format**
Exercises are loaded from a file named `Workout_List.txt`. The file should follow this format:
```
Chest
1. Bench Press
2. Incline Dumbbell Press
...
Shoulders
1. Overhead Press
2. Lateral Raises
...
```
Ensure each category is followed by numbered exercises.

---

## How to Run

### Prerequisites
- Python 3.6 or higher installed.
- A `Workout_List.txt` file containing categorized exercises.

### Steps
1. Clone or download the project.
2. Place a properly formatted `Workout_List.txt` file in the project directory.
3. Run the program:
   ```bash
   make run
   ```
4. Follow the interactive prompts to input your body type, weight, and muscle gain duration.

### Clean Up
To remove Python-generated files (`__pycache__` and `.pyc` files):
```bash
make clean
```

---

## Technical Highlights

### Key Functions
1. **`calculate_calorie_formula`**:
   - Computes daily caloric needs based on body type, weight, and goals.

2. **`generate_schedule`**:
   - Creates a workout schedule with dynamically selected exercises and personalized sets/reps.

3. **`load_workouts`**:
   - Parses `Workout_List.txt` to load exercises into categories.

4. **`main`**:
   - Manages user interaction and orchestrates the program.

### Randomization for Variety
The `random.sample` method ensures that exercises are selected randomly, making every generated schedule unique.

### Error Handling
- Checks for missing or malformed `Workout_List.txt` file.
- Validates user input for body type and fitness goals.

---

## Example Output


<img width="942" alt="Screenshot 2025-01-21 at 9 02 07 PM" src="https://github.com/user-attachments/assets/36a0a383-398e-4e75-bc50-2e080e76ab8f" />


## Future Improvements
- Add export functionality to save schedules as PDFs or CSVs.
- Enhance the calorie calculator with more precise metabolic rate formulas.


