from flask.cli import with_appcontext
import click

from src.ext import db
from src.models import User, WorkoutPlan, WorkoutPlanExercise
from src.models import Exercise


def init_db():
    db.drop_all()
    db.create_all()

def populate_db():
    exercises = [
        {"id": 1, "name": "Push-up", "description": "Basic upper body exercise",
         "instruction": "Keep back straight, lower chest to floor, push up",
         "target_muscle": "chest, triceps, shoulders"},
        {"id": 2, "name": "Plank", "description": "Core stability exercise",
         "instruction": "Hold body straight on forearms and toes", "target_muscle": "abs, back"},
        {"id": 3, "name": "Lunges", "description": "Single-leg lower body exercise",
         "instruction": "Step forward, lower hips, return", "target_muscle": "quadriceps, glutes, hamstrings"},
        {"id": 4, "name": "Burpees", "description": "Full body cardio exercise",
         "instruction": "Squat, jump to plank, push-up, jump up", "target_muscle": "full body"},
        {"id": 5, "name": "Bicep Curl", "description": "Arm strengthening exercise",
         "instruction": "Curl dumbbells upward, elbows stationary", "target_muscle": "biceps"},
        {"id": 6, "name": "Tricep Dips", "description": "Arm exercise using body weight",
         "instruction": "Lower and raise body using a bench or chair", "target_muscle": "triceps"},
        {"id": 7, "name": "Bench Press", "description": "Chest strength exercise",
         "instruction": "Press barbell from chest upward while lying down",
         "target_muscle": "chest, triceps, shoulders"},
        {"id": 8, "name": "Deadlift", "description": "Strength exercise for posterior chain",
         "instruction": "Lift barbell from floor, keeping back straight", "target_muscle": "back, glutes, hamstrings"},
        {"id": 9, "name": "Pull-up", "description": "Upper body pulling exercise",
         "instruction": "Pull body up on a bar until chin over bar", "target_muscle": "back, biceps"},
        {"id": 10, "name": "Sit-up", "description": "Abdominal exercise",
         "instruction": "Lie on back, lift torso towards knees", "target_muscle": "abs"},
        {"id": 11, "name": "Mountain Climbers", "description": "Cardio and core exercise",
         "instruction": "Alternate bringing knees to chest from plank", "target_muscle": "abs, legs, shoulders"},
        {"id": 12, "name": "Leg Raises", "description": "Lower abdominal exercise",
         "instruction": "Lie on back, lift legs straight up and down", "target_muscle": "lower abs"},
        {"id": 13, "name": "Shoulder Press", "description": "Overhead press for shoulders",
         "instruction": "Press dumbbells or barbell overhead", "target_muscle": "shoulders, triceps"},
        {"id": 14, "name": "Jumping Jacks", "description": "Cardio warm-up exercise",
         "instruction": "Jump while moving arms and legs outward", "target_muscle": "full body"},
        {"id": 15, "name": "Russian Twist", "description": "Oblique exercise",
         "instruction": "Sit, twist torso side to side holding weight", "target_muscle": "abs, obliques"},
        {"id": 16, "name": "Calf Raise", "description": "Lower leg exercise",
         "instruction": "Stand on toes, lift and lower heels", "target_muscle": "calves"},
        {"id": 17, "name": "Glute Bridge", "description": "Hip and glute exercise",
         "instruction": "Lie on back, lift hips upward, squeeze glutes",
         "target_muscle": "glutes, hamstrings, lower back"},
        {"id": 18, "name": "Side Plank", "description": "Core stabilization exercise",
         "instruction": "Hold body sideways on forearm and feet", "target_muscle": "obliques, abs"},
        {"id": 19, "name": "Jump Squat", "description": "Plyometric lower body exercise",
         "instruction": "Perform squat, then jump explosively", "target_muscle": "quadriceps, glutes, calves"},
        {"id": 20, "name": "Squat", "description": "Leg and glute exercise",
         "instruction": "Feet shoulder-width, lower hips, keep back straight",
         "target_muscle": "quadriceps, glutes, hamstrings"}
    ]
    for exercise in exercises:
        new_exercise = Exercise(name=exercise["name"], description=exercise["description"], instruction=exercise["instruction"],
                              target_muscle=exercise["target_muscle"])
        db.session.add(new_exercise)
    db.session.commit()

    User(username="User1", password="password123").create()
    User(username="User2", password="password456").create()

    WorkoutPlan(user_id = "1", name = "WorkoutPlan1", frequency = "1", goal = "goal1", daily_duration = "1").create()
    WorkoutPlan(user_id = "2", name = "WorkoutPlan2", frequency = "2", goal = "goal2", daily_duration = "2").create()

    WorkoutPlanExercise(workout_plan_id = "1", exercise_id = "1", sets = "1", repetitions = "1", duration = "1", distance = "1.1").create()
    WorkoutPlanExercise(workout_plan_id = "2", exercise_id = "2", sets = "2", repetitions = "2", duration = "2", distance = "1.12").create()


@click.command("init_db")
@with_appcontext
def init_db_command():
    click.echo("initializing database...")
    init_db()
    click.echo("Initialized database")


@click.command("populate_db")
@with_appcontext
def populate_db_command():
    populate_db()