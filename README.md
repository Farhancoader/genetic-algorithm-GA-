# 🧬 String Breeding Using Genetic Algorithm

An interactive visualization of a **Genetic Algorithm (GA)** that evolves random strings into a target phrase using concepts inspired by natural evolution.

This project implements core evolutionary computation concepts:

- Selection
- Crossover
- Mutation
- Fitness evaluation
- Evolution across generations

Built from scratch using Python and deployed as an interactive Streamlit application.

---

## 🚀 Live Demo

Try the application here:

https://string-breeding-algo.streamlit.app/

---

## 📌 Project Overview

A Genetic Algorithm is an optimization technique inspired by biological evolution.

The algorithm starts with a population of random strings and improves them over multiple generations until the target string is discovered.

### Evolution Process

```
Random Population
        ↓
Fitness Evaluation
        ↓
Parent Selection
        ↓
Crossover
        ↓
Mutation
        ↓
New Generation
        ↓
Repeat Until Target Found
```

Example:

```
Target:
hello world

Generation 0:
fewmostpsaf

Generation 15:
hellowworld

Generation 34:
hello world
```

---

# 🧠 How It Works

## 1. Fitness Function

Each individual is evaluated based on how many characters match the target string.

Formula:

```
Fitness = Matching Characters / Total Characters
```

Example:

```
Target:
hello world

Individual:
hellx worlz

Fitness:
9/11 = 81.8%
```

Individuals with higher fitness values have a better chance of contributing to future generations.

---

## 2. Selection

The algorithm selects parents based on their fitness score.

Higher-performing individuals are more likely to be selected, simulating the idea of:

> Survival of the fittest

---

## 3. Crossover

Crossover combines genetic information from two parents to create a new child.

Example:

```
Parent 1:
hello abcde

Parent 2:
hello world

Child:
hello worle
```

---

## 4. Mutation

Mutation introduces random changes into the population.

This helps maintain diversity and prevents the algorithm from getting stuck.

Example:

```
Before:
hellx worle

After:
hello world
```

---

# ✨ Features

## Genetic Algorithm

- Genetic Algorithm implemented from scratch
- Object-oriented design
- Elite preservation
- Probability-based parent selection
- Configurable mutation rate

## Streamlit Interface

- Interactive web interface
- Custom target string input
- Adjustable population size
- Adjustable mutation rate
- Adjustable evolution speed
- Real-time fitness visualization
- Generation tracking
- Completion animation

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Object-Oriented Programming
- Genetic Algorithms
- Randomized Optimization

---

# 📂 Project Structure

```
genetic-algorithm-GA-
│
├── main.py
│   └── Streamlit application and Genetic Algorithm implementation
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
    └── Documentation
```

---

# ⚙️ Installation & Usage

## Clone Repository

```bash
git clone https://github.com/Farhancoader/genetic-algorithm-GA-.git
```

## Navigate to Project

```bash
cd genetic-algorithm-GA-
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run main.py
```

The application will open at:

```
http://localhost:8501
```

---

# 📈 Future Improvements

Possible extensions:

- Character-level color visualization
- Average fitness vs best fitness comparison
- Evolution animation export
- Tournament selection
- Adaptive mutation rates
- Applying Genetic Algorithms to:
  - Travelling Salesman Problem
  - Feature selection
  - Neural network optimization

---

# 🎯 Learning Outcomes

Through this project, I explored:

- How Genetic Algorithms work internally
- Evolutionary optimization techniques
- Object-oriented algorithm design
- Building interactive AI visualizations
- Deploying Python applications using Streamlit

---

# 👨‍💻 Author

**Farhan Baig**

GitHub:
https://github.com/Farhancoader
