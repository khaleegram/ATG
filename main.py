from csp_module import csp_schedule
from ml_module import train_ml_model
from ga_module import ga_schedule

# Define your data
venues = [
    {"id": 1, "name": "Auditorium", "capacity": 300},
    {"id": 2, "name": "Lecture Hall A", "capacity": 100},
]
time_slots = ["Monday 08:00-10:00", "Monday 10:00-12:00"]
courses = [
    {"id": 1, "name": "Math 101", "students": 80},
    {"id": 2, "name": "Physics 101", "students": 50},
]

# CSP
csp_solutions = csp_schedule(venues, time_slots, courses)

# Print CSP solutions
if csp_solutions:
    print("CSP Generated Solutions:")
    for solution in csp_solutions:
        print(solution)
else:
    print("No solution found!")

# ML
ml_model = train_ml_model()
for course in courses:
    for venue in venues:
        features = [[course["students"], venue["capacity"]]]
        popularity = ml_model.predict(features)
        print(f"Popularity for {course['name']} in {venue['name']}: {popularity[0]}")

# GA
ga_population = ga_schedule(courses, venues, time_slots)

# Display final population
print("Final GA Population:")
for individual in ga_population:
    print(individual)