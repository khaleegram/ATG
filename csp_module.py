from constraint import Problem

def csp_schedule(venues, time_slots, courses):
    problem = Problem()

    # Transform data for CSP compatibility
    course_names = [course["name"] for course in courses]
    venue_time_pairs = [(venue["name"], time) for venue in venues for time in time_slots]

    # Define variables for each course and their domains
    problem.addVariables(course_names, venue_time_pairs)

    # Venue capacity constraint
    def venue_capacity_constraint(*assignments):
        assignment_dict = dict(zip(course_names, assignments))
        for course, (venue, time) in assignment_dict.items():
            for other_course, (other_venue, other_time) in assignment_dict.items():
                if course != other_course and time == other_time and venue == other_venue:
                    return False  # Ensure no venue is double-booked
        return True

    problem.addConstraint(venue_capacity_constraint, course_names)

    # Return solutions
    return problem.getSolutions()
