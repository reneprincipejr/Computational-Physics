import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import sin, cos
from scipy.integrate import odeint

def derivs(y, T):
    return np.array([y[1], - r*y[1] - sin(y[0]) + a*cos(w_d*T)], dtype = float)

#y[0] = phi
#y[1] = omega
y = (np.pi/2, 0) 
y_states = np.radians(y)


N = 100000
pstep = 3*np.pi

#constants
r = 0.25
a = 0.7
w_d = 2/3

#time array
dt = 0.1
T = np.arange(0.0, N, dt)
t_j = 2*np.pi*T/w_d

# solves for the odeint  # returns phi and omega
y = odeint(derivs, y_states, T)

#plt.plot(y[:,0],y[:,1], linewidth = 0.5)
#plt.xlim(-np.pi,np.pi)
#plt.ylim(-np.pi,np.pi)
#plt.rcParams["figure.figsize"] = [12,8]
#plt.title("PHASESPACE PLOT for "
#          "r = 0.25, a = 0.7000")
#plt.xlabel('$\phi$', size='xx-large')
#plt.ylabel('$\omega$', size='xx-large')
#plt.show()


xx = y[:,0]
yy = y[:,1]

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated = True)

def init():
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-np.pi, np.pi)
    return ln,

def update(frame):
    xdata.append(xx[frame])
    ydata.append(yy[frame])
    ln.set_data(np.concatenate(xdata, ydata))
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0,N),
                    init_func=init, blit=True)

ani.save('chaotic_pendulum.html', fps=15)
plt.show()
