import random
import string

ALPHABET = string.ascii_lowercase + " "

class DNA:
    def __init__(self,length:int):
        self.genes = [random.choice(ALPHABET) for _ in range(length)]
        self.fitness = 0

    def __str__(self):
        return "".join(self.genes)

    def calculate_fitness(self,target):
        matches = 0
        for g, t in zip(self.genes, target):
            if g == t:
                matches += 1
        self.fitness = matches/len(target)

    def crossover(self, partner):

        child = DNA(len(self.genes))

        for i in range(len(self.genes)):
            if random.random() < 0.5:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]

        return child

    def mutate(self, mutation_rate):

        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = random.choice(ALPHABET)

class Population:
    def __init__(self,size,target):
        self.target = target
        self.members = [DNA(len(target)) for _ in range(size)]

    def evaluate(self):
        for dna in self.members:
            dna.calculate_fitness(self.target)

    def select_parent(self):

        total_fitness = sum(
            dna.fitness for dna in self.members
        )

        if total_fitness == 0:
            return random.choice(self.members)

        return random.choices(
            self.members,
            weights=[
                dna.fitness for dna in self.members
            ],
            k=1
        )[0]

    def evolve(self, mutation_rate):

        elite = self.best()

        new_members = [elite]

        while len(new_members) < len(self.members):

            p1 = self.select_parent()
            p2 = self.select_parent()

            child = p1.crossover(p2)
            child.mutate(mutation_rate)

            new_members.append(child)

        self.members = new_members

    def best(self):
        return max(
            self.members,
            key=lambda dna: dna.fitness
        )
    def finished(self):

        return self.best().fitness == 1

target = "hello world"

pop = Population(100, target)

generation = 0

while True:

    pop.evaluate()

    best = pop.best()

    print(
        f"Generation {generation}:",
        best,
        best.fitness
    )

    if pop.finished():
        break

    pop.evolve(0.01)

    generation += 1