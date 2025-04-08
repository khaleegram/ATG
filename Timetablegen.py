import random
from constraint import Problem


# Step 1: Define Input Data
venues = [
    {"name": "Lecture Hall 1", "capacity": 50},
    {"name": "Lecture Hall 2", "capacity": 100},
    {"name": "Lecture Hall 3", "capacity": 80},
    {"name": "Computer Lab", "capacity": 40},
    {"name": "Auditorium", "capacity": 200},
]

courses = [
    {"name": "Math 101", "students": random.randint(20, 100)},
    {"name": "Physics 101", "students": random.randint(20, 100)},
    {"name": "Chemistry 101", "students": random.randint(20, 100)},
    {"name": "Biology 101", "students": random.randint(20, 100)},
    {"name": "English 101", "students": random.randint(20, 100)},
    {"name": "History 101", "students": random.randint(20, 100)},
    {"name": "Geography 101", "students": random.randint(20, 100)},
    {"name": "Computer Science 101", "students": random.randint(20, 100)},
    {"name": "Economics 101", "students": random.randint(20, 100)},
    {"name": "Sociology 101", "students": random.randint(20, 100)},
    {"name": "Law 101", "students": random.randint(20, 100)},
    {"name": "Medicine 101", "students": random.randint(20, 100)},
    {"name": "Engineering 101", "students": random.randint(20, 100)},
    {"name": "Philosophy 101", "students": random.randint(20, 100)},
    {"name": "Business 101", "students": random.randint(20, 100)},
    {"name": "Statistics 101", "students": random.randint(20, 100)},
    {"name": "Psychology 101", "students": random.randint(20, 100)},
    {"name": "Political Science 101", "students": random.randint(20, 100)},
    {"name": "Fine Arts 101", "students": random.randint(20, 100)},
    {"name": "Music 101", "students": random.randint(20, 100)},
]

instructors = [
    "Dr. Smith", "Dr. Johnson", "Dr. Brown", "Dr. Williams",
    "Dr. Jones", "Dr. Miller", "Dr. Davis", "Dr. Garcia", "Dr. Martinez"
]

time_slots = [
    {"day": day, "time": f"{hour}:00-{hour + 2}:00"}
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for hour in [8, 10, 12, 2, 4] if not (hour == 1 or (hour == 12 and day != "Saturday"))
]

# Break Time Constraint
break_time = {"start": 1, "end": 2}

# Step 2: CSP Implementation
def generate_timetable():
    problem = Problem()

    # Add variables
    for course in courses:
        problem.addVariable(
            course["name"],
            [(venue["name"], slot["day"], slot["time"]) for venue in venues for slot in time_slots]
        )

    # Add constraints
    def no_overlap(*assignments):
        schedule = {}
        for course, (venue, day, time) in zip(courses, assignments):
            if day not in schedule:
                schedule[day] = []
            for existing_time in schedule[day]:
                if existing_time == time:  # Overlap in time
                    return False
            schedule[day].append(time)
        return True

    problem.addConstraint(no_overlap, [course["name"] for course in courses])

    def respect_capacity(course_name, venue_name, *_):
        course = next(c for c in courses if c["name"] == course_name)
        venue = next(v for v in venues if v["name"] == venue_name)
        return course["students"] <= venue["capacity"]

    for course in courses:
        problem.addConstraint(respect_capacity, (course["name"], course["name"]))

    # Solve the CSP
    solution = problem.getSolution()
    return solution

# Step 3: Genetic Algorithm for Optimization
def optimize_timetable(timetable):
    def fitness(solution):
        # Optimization criteria: minimize gaps, balance workload
        gap_penalty = 0
        instructor_penalty = 0

        instructor_schedule = {instructor: [] for instructor in instructors}
        for course, (venue, day, time) in solution.items():
            assigned_instructor = random.choice(instructors)
            instructor_schedule[assigned_instructor].append((day, time))

        for instructor, schedule in instructor_schedule.items():
            schedule.sort(key=lambda x: x[1])
            for i in range(1, len(schedule)):
                gap_penalty += abs(schedule[i][1] - schedule[i - 1][1])

        return -gap_penalty - instructor_penalty

    # Placeholder for GA logic (initial population, selection, crossover, mutation)
    optimized_solution = timetable  # Simplified for now
    return optimized_solution

# Step 4: Main Function
if __name__ == "__main__":
    initial_timetable = generate_timetable()
    print("\nInitial Timetable (CSP):\n", initial_timetable)

    optimized_timetable = optimize_timetable(initial_timetable)
    print("\nOptimized Timetable (GA):\n", optimized_timetable)
