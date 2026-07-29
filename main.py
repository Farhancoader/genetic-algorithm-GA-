import streamlit as st
import random
import string
import time

ALPHABET = string.ascii_lowercase + " "


# =======================
# Genetic Algorithm
# =======================

class DNA:
    def __init__(self, length: int):
        self.genes = [random.choice(ALPHABET) for _ in range(length)]
        self.fitness = 0

    def __str__(self):
        return "".join(self.genes)

    def calculate_fitness(self, target):
        matches = 0
        for g, t in zip(self.genes, target):
            if g == t:
                matches += 1
        self.fitness = matches / len(target)

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
    def __init__(self, size, target):
        self.target = target
        self.members = [DNA(len(target)) for _ in range(size)]

    def evaluate(self):
        for dna in self.members:
            dna.calculate_fitness(self.target)

    def select_parent(self):
        total = sum(dna.fitness for dna in self.members)

        if total == 0:
            return random.choice(self.members)

        return random.choices(
            self.members,
            weights=[dna.fitness for dna in self.members],
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
        return max(self.members, key=lambda dna: dna.fitness)

    def finished(self):
        return self.best().fitness == 1


# =======================
# Streamlit UI
# =======================

st.set_page_config(
    page_title="String Breeding",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 String Breeding using Genetic Algorithm")
st.write("Watch a population evolve until it matches the target string.")

st.sidebar.header("Settings")

target = st.sidebar.text_input(
    "Target String",
    "hello world"
)

population_size = st.sidebar.slider(
    "Population Size",
    20,
    1000,
    100
)

mutation_rate = st.sidebar.slider(
    "Mutation Rate",
    0.0,
    0.20,
    0.01,
    step=0.005
)

speed = st.sidebar.slider(
    "Animation Delay (seconds)",
    0.0,
    0.5,
    0.02,
    step=0.01
)

start = st.sidebar.button("🚀 Start Evolution")

if start:

    pop = Population(population_size, target)

    generation_placeholder = st.empty()
    string_placeholder = st.empty()
    progress_placeholder = st.empty()
    stats_placeholder = st.empty()
    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    generation = 0
    history = []

    for generation in range(10000):

        pop.evaluate()

        best = pop.best()

        history.append(best.fitness)

        generation_placeholder.subheader(
            f"Generation {generation}"
        )

        string_placeholder.code(str(best), language=None)

        progress_placeholder.progress(best.fitness)

        stats_placeholder.metric(
            "Fitness",
            f"{best.fitness*100:.2f}%"
        )

        chart_placeholder.line_chart(history)

        log_placeholder.text(
            f"Best Individual : {best}\n"
            f"Fitness         : {best.fitness:.4f}\n"
            f"Generation      : {generation}"
        )

        if pop.finished():
            st.success("🎉 Target reached!")
            st.balloons()
            break

        pop.evolve(mutation_rate)


        time.sleep(speed)