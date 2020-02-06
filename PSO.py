import numpy as np
import random as rnd
from stoch_optim_utilities import check_bounds

def PSO(f, num_par, bounds, max_iter, c1, c2, w, w_red):
    '''
    ------------------------------
    PARTICLE SWARM OPTIMIZATION
    ------------------------------
    --- Input ---
    f: (function) Objetive function
    num_par: (integer) Number of particles in the swarm
    bounds: (list) Lower and higer bounds for each variable in the funtion
    max_iter: (integer) Maximum number of iterations
    c1: (float) Cognition
    c2: (float) Social behavior
    w: (float) Inertia weight
    w_red: (float) Reduction parameter of w at each iteration (w = w*w_red)
   
    --- Output ---
    Optimum: (class) Results with:
        Optimum.f: (float) The best value of the funtion found in the optimization
        Optimum.x: (array) The best point in which the function was evaluated
        Optimum.traj: (matrix) Column 0: Number of iteration. Column 1: Value for current iteration
    '''
    S             = num_par
    dim           = len(bounds)
    trajectory_f  = np.zeros((max_iter, 2)) # Storage of optimization trajectory
    trajectory_p  = np.array([np.zeros((S, dim)) for i in range(max_iter)])
    
    # Random initial positions and initial velocities set to zero
    p         = np.array([[rnd.uniform(bounds[i][0],bounds[i][1]) for i in range(dim)] for p in range(S)]) 
    p_best_p  = p 
    p_best_v  = [f(p_best_p[i]) for i in range(S)]
    v         = np.array([[(0) for i in range(dim)] for p in range(S)])
    
    # Best position and function value of the swarm
    min_v    = min(p_best_v) 
    s_best_p = p_best_p[np.where(p_best_v == min_v)[0][0]]
    
    iter_count = 0
    # Stores trajectory
    trajectory_f[iter_count][0] = iter_count
    trajectory_f[iter_count][1] = min_v
    trajectory_p[iter_count] = p
    
    #Iteration Loop    
    while iter_count < max_iter-1:
        r1 = np.array([[rnd.uniform(0,1) for i in range(dim)] for p in range(S)])
        r2 = np.array([[rnd.uniform(0,1) for i in range(dim)] for p in range(S)])
        # Update velocities
        v  = w*v + c1*r1*(p_best_p - p) + c2*r2*(s_best_p - p)
        # Update position
        p  = p + v
        #Check if the new position is within the bounds, if not it assigns it as the best known position by the particle so far
        for particle in range(S):
            check = check_bounds(bounds, p[particle])
            if not check:
                p[particle] = p_best_p[particle]
            # Update the best current position and function value for each particle
            if f(p[particle]) < p_best_v[particle]:
                p_best_p[particle] = p[particle]
                p_best_v[particle] = f(p[particle])
        # Updates best position of the swarm
        cur_min = min(p_best_v)
        if cur_min < min_v:
            min_v    = cur_min
            s_best_p = p_best_p[np.where(p_best_v == min_v)[0][0]]
        # Reduce w
        w          *= w_red
        iter_count += 1
        # Stores trajectory
        trajectory_f[iter_count][0] = iter_count
        trajectory_f[iter_count][1] = min_v
        trajectory_p[iter_count]    = p
        
    # Gather results
    class Optimum:
        pass
    Optimum.f         = f(s_best_p)
    Optimum.x         = s_best_p
    Optimum.traj_f    = trajectory_f
    Optimum.traj_p    = trajectory_p
    
    return Optimum