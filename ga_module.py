from deap import base, creator, tools, algorithms
import random

def ga_schedule(courses, venues, time_slots):
    # Define the fitness and individual types
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    toolbox = base.Toolbox()

    # Attribute generators
    toolbox.register("attr_time", random.choice, time_slots)
    toolbox.register("attr_venue", random.choice, venues)

    # Individual is a list of (time, venue) pairs
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                     lambda: (toolbox.attr_time(), toolbox.attr_venue()), n=len(courses))

    # Population is a list of individuals
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Evaluation function
    def evaluate(individual):
        penalty = 0
        for course, (time, venue) in zip(courses, individual):
            if course["students"] > venue["capacity"]:
                penalty += 1  # Add penalty if venue capacity is exceeded
        return (penalty,)

    # Custom mutation function
    def mutCustom(individual):
        for i in range(len(individual)):
            if random.random() < 0.1:  # Mutation probability for each gene
                individual[i] = (random.choice(time_slots), random.choice(venues))
        return (individual,)

    # Genetic operators
    toolbox.register("evaluate", evaluate)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", mutCustom)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Initialize population
    population = toolbox.population(n=50)

    # Apply genetic algorithm
    algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, verbose=True)

    # Return the final population
    return population
