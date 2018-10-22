import numpy.random
from solver import SATInstance

MAX_NONIMPROVING_MOVES = 10

instance = SATInstance()
instance.from_file('dimacs.txt')
instance.create_random_assignment()
print('+++ Start +++')
print('First assignment: ', instance.variables)

satisfied = instance.count_satisfied_clauses(instance.variables)
print('Clauses satisfied: ', satisfied, '\n\n')
mostSatisfied = satisfied
movesSinceImprovement = 0
change = int()
step = 1
while mostSatisfied < len(instance.clauses) and movesSinceImprovement < MAX_NONIMPROVING_MOVES:
    change = instance.find_next_assignment()
    satisfied = satisfied + change
    if satisfied > mostSatisfied:
        mostSatisfied = satisfied
        movesSinceImprovement = 0
    else:
        movesSinceImprovement = movesSinceImprovement + 1
    print('=== New assignment ===')
    print('Step ', step)
    print('Assignment: ', instance.variables)
    print('Clauses satisfied: ', satisfied)
    print('Most satisfied: ', mostSatisfied)
    print('Moves since improvement: ', movesSinceImprovement, '\n')
    step = step + 1
