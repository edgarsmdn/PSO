# Particle Swarm Optimization

<p align="center">
<img src="https://github.com/edgarsmdn/PSO/blob/master/PSO_1.gif" width="500"> 
</p>

## Development

This work was part of the project I did during my undergrad research internship in the summer of 2018 at the [Centre for Process Integration](https://www.ceas.manchester.ac.uk/cpi/), The University of Manchester on stochastic optimization.

## Background

Particle Swarm Optimization (PSO) is a stochastic optimization algorithm inspired by the behavior of several animal communities. It implements two important variables, cognition and social behaviour, in an attempt to mimic the intelligence of such communities. This algorithm was firstly proposed by Kennedy and Eberhart (1995). The algorithm is initialized with a set of points (particles) randomly distributed within the search space. The postion and velocity of these particles is progressively updated according to the two main parameters mentioned above: cognition (self-confidence) and social behaviour (population-confidence). At each iteration the particles remember their own best position visited so far, and the best position visited by the swarm as a whole. They adjust their velocity and position taking into account both best values (individual and collective) to explore the search space collectively. In this way, the swarm attempts to move towards the global optimum.

The equations that describe the velocity and position of the particles at each iteration are:

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?v_i%5E%7Bt&plus;1%7D%20%3D%20w%20%7E%20v_i%5E%7Bt%7D%20&plus;%20c_1%20%7E%20r_1%20%7E%20%28x_%7Bi%2Cb%7D%5E%7Bt%7D%20-%20x_i%5E%7Bt%7D%29%20&plus;%20c_2%20%7E%20r_2%20%7E%20%28x_%7Bg%2Cb%7D%5E%7Bt%7D%20-%20x_i%5E%7Bt%7D%29">
</p>

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?x_i%5E%7Bt&plus;1%7D%20%3D%20x_i%5Et%20&plus;%20v_i%5E%7Bt&plus;1%7D">
</p>

where 
![equation](https://latex.codecogs.com/gif.latex?v) and ![equation](https://latex.codecogs.com/gif.latex?x) are the velocity and the postion of the particle ![equation](https://latex.codecogs.com/gif.latex?i) respectively; ![equation](https://latex.codecogs.com/gif.latex?w) is an scaling factor (a.k.a. inertia weight) that prevents the exponential growth of the velocity at each iteration; ![equation](https://latex.codecogs.com/gif.latex?t) stands for the current iteration; ![equation](https://latex.codecogs.com/gif.latex?c_1) and ![equation](https://latex.codecogs.com/gif.latex?c_2) are the cognition and population-confidence parameters respectively; ![equation](https://latex.codecogs.com/gif.latex?r_1) and ![equation](https://latex.codecogs.com/gif.latex?r_2) are random variables uniformly distributed between 0 and 1; ![equation](https://latex.codecogs.com/gif.latex?b) denotes the best position found so far and ![equation](https://latex.codecogs.com/gif.latex?g) denotes the best position found until the current iteration by the whole swarm. 

## Prerequisites

The function requires Python 3.0 (or more recent versions). The *stoch_optim_utilities.py* file (which contains common utilities needed in stochastic optimization algorithms) needs to be in the same directory as the function file *PSO.py*.

## Functioning

#### Inputs

```
PSO(f, num_par, bounds, max_iter, c1, c2, w, w_red)
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. The **function** to be optimized. The functions needs to be of the form ![equation](https://latex.codecogs.com/gif.latex?%5Cmathbb%7BR%7D%5En%20%5Crightarrow%20%5Cmathbb%7BR%7D).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. The **number of particles**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. The **bounds** for each dimension of the fucntion. This has to be a list of the form `[(lb1, ub1), (1b2, ub2), ...]`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4. The **maximum number of iterations** which is the stopping criteria in this implementation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5. The **cognition** parameter as an integer or float.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6. The **social-confidence** parameter as an integer or float.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7. The **inertia weight** parameter as an integer or float.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 8. The **reduction parameter** ![equation](https://latex.codecogs.com/gif.latex?w_%7Bred%7D). This reduces the inertia weight at each iteration following: ![equation](https://latex.codecogs.com/gif.latex?w%5E%7Bt&plus;1%7D%3D%20w_%7Bred%7D%20%7E%20w%5Et) 

#### Outputs

```
Optimum: (class) Results with:
        Optimum.f: (float) The best function value found in the optimization
        Optimum.x: (array) The best point in which the function was evaluated
        Optimum.traj_f: (array) Trajectory of function values
        Optimum.traj_x: (array) Trajectory of positions
```

#### General information

* In this implementation the initial position of the particles is set randomly, while their initial velocities are set to zero. 

* The random constants are updated at each iteration to a random value uniformly distributed between 0 and 1. 

* The stoping criteria implemented in this algrithm is a maximum number of iterations defined by the user.

* The file *example_PSO.py* exemplify the use of the optimization algorithm.

### References
Kennedy, J. and Eberhart, R., 1995, November. Particle swarm optimization. In Proceedings of ICNN'95-International Conference on Neural Networks (Vol. 4, pp. 1942-1948). IEEE.

A. Kaveh, Advances in Metaheuristic Algorithms for Optimal Design of Structures, Chapter 2. Particle Swarm Optimization,
DOI 10.1007/978-3-319-46173-1_2
