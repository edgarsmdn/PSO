# Particle Swarm Optimization

<p align="center">
<img src="https://github.com/edgarsmdn/PSO/blob/master/PSO.gif" width="500"> 
</p>

## Development

This work was part of the project I did during my undergrad research internship in the summer of 2018 at the [Centre for Process Integration](https://www.ceas.manchester.ac.uk/cpi/), The University of Manchester on stochastic optimization.

## Background

Particle Swarm Optimization (PSO) is an stochastic optimization algorithm inspired by the behavior of several animal communities. It implements two important variables: cognition and social behaviour. This algorithm was firstly proposed by Kennedy and Eberhart (1995). The algorithm is initialized with a set of points (particles) randomly distributed within the search space. The postion and velocity of these particles is progressively updated according to two main parameters: cognition (self-confidence) and social behaviour (population-confidence). At each iteration the particles remember their own best position visited so far, and the best position visited by the swarm as a whole. They adjust their velocity and position taking into account both best values (individual and collective) in an attempt to mimic the intelligence of animal comunities. In this way, the swarm attempts to move towards the global optimum.

The equations that describe the velocity and position of the particles at each iteration are:

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?v_i%5E%7Bt&plus;1%7D%20%3D%20w%20%7E%20v_i%5E%7Bt%7D%20&plus;%20c_1%20%7E%20r_1%20%7E%20%28x_%7Bi%2Cb%7D%5E%7Bt%7D%20-%20x_i%5E%7Bt%7D%29%20&plus;%20c_2%20%7E%20r_2%20%7E%20%28x_%7Bg%2Cb%7D%5E%7Bt%7D%20-%20x_i%5E%7Bt%7D%29">
</p>

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?x_i%5E%7Bt&plus;1%7D%20%3D%20x_i%5Et%20&plus;%20v_i%5E%7Bt&plus;1%7D">
</p>

where 
![equation](https://latex.codecogs.com/gif.latex?v) and ![equation](https://latex.codecogs.com/gif.latex?x) are the velocity and the postion of the particle ![equation](https://latex.codecogs.com/gif.latex?i) respectively; ![equation](https://latex.codecogs.com/gif.latex?w) is an scaling factor (a.k.a. inertia weight) that prevents the exponential growth of the velocity at each iteration; ![equation](https://latex.codecogs.com/gif.latex?t) stands for the current iteration; ![equation](https://latex.codecogs.com/gif.latex?c_1) and ![equation](https://latex.codecogs.com/gif.latex?c_2) are the cognition and population-confidence parameters respectively; ![equation](https://latex.codecogs.com/gif.latex?r_1) and ![equation](https://latex.codecogs.com/gif.latex?r_2) are random variables uniformly distributed between 0 and 1; ![equation](https://latex.codecogs.com/gif.latex?b) denotes the best position found so far and ![equation](https://latex.codecogs.com/gif.latex?g) denotes the best position found until the current iteration by the whole swarm. 


In this implementation the initial position of the particles is set randomly, while the initial velocity is set to zero. The cognition and social constants were set to 2. The random constants were updated at each iteration to a random value uniformly distributed between 0 and 1.

## Prerequisites

The function requires Python 3.0 (or more recent versions). The *stoch_optim_utilities.py* file needs to be in the same directory as the function file *PSO.py*.

## Functioning

The stop criteria is the maximum number of iterations defined by the user.

### References
Kennedy, J. and Eberhart, R., 1995, November. Particle swarm optimization. In Proceedings of ICNN'95-International Conference on Neural Networks (Vol. 4, pp. 1942-1948). IEEE.

A. Kaveh, Advances in Metaheuristic Algorithms for Optimal Design of Structures, Chapter 2. Particle Swarm Optimization,
DOI 10.1007/978-3-319-46173-1_2
