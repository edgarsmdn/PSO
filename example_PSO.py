from PSO import PSO
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

'''

                              Example of PSO 

'''

def alpine1(variables):
    '''
    Alpine 1 function
    Minimum at 0 at x = [zeros]
    Usually domain of evaluation is [-10, 10]
    Source: http://infinity77.net/global_optimization/test_functions_nd_A.html#n-d-test-functions-a
    Retrieved: 19/06/2018
    '''
    return np.sum(np.abs(np.multiply(variables, np.sin(variables)) + 0.1 * variables))

f = alpine1
b = (-10, 10)

# Optimization using PSO
num_par  = 40
bounds   = [b for i in range(2)] 
max_iter = 60
c1       = 2
c2       = 2
w        = 1
w_red    = 0.8

results = PSO(f, num_par, bounds, max_iter, c1, c2, w, w_red)

# Plot Optimization

particles             = np.zeros(num_par, dtype=[("position", float, 2)])
particles["position"] = results.traj_p[0]

fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 
start, stop, n_values = b[0], b[1], 100

x       = np.linspace(start, stop, n_values)
y       = np.linspace(start, stop, n_values)
X, Y    = np.meshgrid(x, y)
zs = np.array([f(np.array([x,y])) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z  = zs.reshape(X.shape)

cm = plt.contourf(X, Y, Z, cmap='Blues')
plt.colorbar(cm)
ax.set_title('Apline 1 function')
ax.set_xlabel('x')
ax.set_ylabel('y')

scatter = ax.scatter(particles["position"][:,0], particles["position"][:,1], c='red', s=4)

def update(frame_number):
    particles["position"] = results.traj_p[frame_number]
    scatter.set_offsets(particles["position"])
    return scatter, 

anim = FuncAnimation(fig, update, interval=200, frames=range(max_iter))
plt.show() 

# Save gif
anim.save('PSO.gif', writer='imagemagick', fps=10)