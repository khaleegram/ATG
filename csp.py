from ortools.sat.python import cp_model

def create_timetable(courses, rooms, instructors, time_slots):
    model = cp_model.CpModel()
    schedule = {}

    # Create variables for each course
    for course in courses:
        schedule[course] = {
            'room': model.NewIntVar(0, len(rooms) - 1, f"room_{course}"),
            'time': model.NewIntVar(0, len(time_slots) - 1, f"time_{course}"),
        }

    # Add constraints
    for course in courses:
        model.Add(schedule[course]['room'] <= len(rooms) - 1)  # Room exists
        model.Add(schedule[course]['time'] <= len(time_slots) - 1)  # Valid time

    # Dynamic adjustment: Room capacity
    for course in courses:
        if courses[course]['students'] > rooms[schedule[course]['room']]['capacity']:
            model.Add(schedule[course]['room'] != rooms.index(course))  # Reassign room

    # Solve the model
    solver = cp_model.CpSolver()
    solver.Solve(model)

    # Output timetable
    return {course: {'room': solver.Value(schedule[course]['room']),
                     'time': solver.Value(schedule[course]['time'])} for course in courses}

# Example inputs
courses = {'Math101': {'students': 120}, 'Bio102': {'students': 80}}
rooms = [{'name': 'Room A', 'capacity': 100}, {'name': 'Room B', 'capacity': 150}]
time_slots = ['8:00-9:00', '9:00-10:00']

print(create_timetable(courses, rooms, {}, time_slots))
