import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. THE BENCHMARK (The Environment)
# ==========================================
def rastrigin(x):
    """
    Rastrigin function: A complex terrain with many local traps.
    Global minimum is at exactly [0, 0, ..., 0] where fitness = 0.
    """
    A = 10
    return A * len(x) + np.sum(x**2 - A * np.cos(2 * np.pi * x))

# ==========================================
# 2. THE DKO ALGORITHM
# ==========================================
def dragonfly_kinematic_optimization(dim, num_agents, bounds, iterations):
    lower_bound, upper_bound = bounds
    
    # Initialize the dragonfly swarm
    positions = np.random.uniform(lower_bound, upper_bound, (num_agents, dim))
    fitness = np.apply_along_axis(rastrigin, 1, positions)
    
    # Memory: Remember previous fitness for the "Omnidirectional Reversal"
    prev_fitness = np.copy(fitness) 
    
    # Global Best tracking
    global_best_pos = positions[np.argmin(fitness)]
    global_best_fitness = np.min(fitness)
    
    # DKO Hyperparameters
    alpha = 0.8  # Forewing power (Exploration)
    beta = 1.2   # Hindwing power (Exploitation)
    gamma = 0.6  # Evasion multiplier (How fast they reverse out of traps)
    
    convergence_history = []

    for t in range(iterations):
        for i in range(num_agents):
            current_fit = rastrigin(positions[i])
            
            # Update the global best if a dragonfly found a better spot
            if current_fit < global_best_fitness:
                global_best_fitness = current_fit
                global_best_pos = np.copy(positions[i])
            
            # ----------------------------------------------------
            # STEP 1: The Four-Wing Thrust Vectors
            # ----------------------------------------------------
            X_random = np.random.uniform(lower_bound, upper_bound, dim)
            r1 = np.random.rand()
            r2 = np.random.rand()
            
            # Forewings pull towards random areas to explore
            W_f = r1 * (X_random - positions[i])
            
            # Hindwings pull towards the best known target
            W_h = r2 * (global_best_pos - positions[i])
            
            # Base Kinematic Vector
            V = (alpha * W_f) + (beta
          
