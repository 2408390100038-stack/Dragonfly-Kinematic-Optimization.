# Dragonfly Kinematic Optimization (DKO)

**A novel, biologically-inspired optimization algorithm based on individual flight kinematics, omnidirectional reversal, and hydraulic-jet bursting.**

## Overview
While existing metaheuristics such as Mirjalili's Dragonfly Algorithm (2016) focus on the macroscopic swarming behavior of dragonflies, they ignore the insect's most powerful evolutionary advantages: its individual flight mechanics. 

Dragonfly Kinematic Optimization (DKO) is a new continuous optimization algorithm that models the dragonfly's biomechanics to navigate complex, high-dimensional mathematical landscapes. By abandoning slow-turning velocity vectors in favor of a dual-wing/jet-burst system, DKO avoids local minima traps with aggressive, zero-radius maneuvers.

## Core Biomechanical Features

DKO introduces three unique mathematical mechanics to the optimization space:

### 1. Dual-Vector Search (Forewing vs. Hindwing)
Unlike standard algorithms where an agent has a single velocity vector, DKO agents calculate two simultaneous thrust vectors:
* **Forewing Thrust (W_f):** Dedicated to rapid space exploration, pulling the agent toward random coordinate vectors.
* **Hindwing Thrust (W_h):** Dedicated to exploitation, pulling the agent precisely toward the Global Best (G_best).

### 2. Omnidirectional Reversal (Kinematic Evasion)
Standard particles act like airplanes—they must bank and turn to escape a trap. Dragonflies can fly backward. In DKO, if an agent evaluates a position worse than its previous state, it triggers a **Kinematic Evasion Multiplier (gamma)**. The polarity of the wings instantly reverses, aggressively backing the agent out of the local minimum in a single iteration.

### 3. The "Jet Engine" Burst
Dragonflies hover to track prey, then utilize a hydraulic-like burst to capture it. DKO calculates the gradient of improvement. If an agent detects a steep drop in the cost function (smelling the global optimum), a **Jet Burst Multiplier (J)** activates, multiplying the step size to snap to the target and skip over intermediate traps.

## Performance
DKO is highly suited for rugged, multi-dimensional continuous spaces such as:
* Maximum Power Point Tracking (MPPT) in shaded solar arrays.
* Robotic Inverse Kinematics for multi-axis arms.
* Parameter tuning for real-time edge devices.

Due to its reliance on basic vector addition rather than complex tree structures (like FMT*) or matrix inversions, DKO boasts near-zero time complexity per iteration, making it ideal for microcontrollers.

## Usage
Run the included `dko_algorithm.py` to see the swarm solve the 10-Dimensional Rastrigin function, a notoriously difficult benchmark full of local minima traps.

```python
# Initialize and run DKO
from dko_algorithm import dragonfly_kinematic_optimization

best_position, best_score, history = dragonfly_kinematic_optimization(
    dim=10, 
    num_agents=30, 
    bounds=(-5.12, 5.12), 
    iterations=100
)
