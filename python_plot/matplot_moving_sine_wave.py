# Let’s use FuncAnimation to create a basic animation of a sine wave
#  moving across the screen. The source code for the animation has been taken 
# from the Matplotlib Animation tutorial. Let’s first see the output and then
#  we shall break down the code to understand what’s going under the hood.

# ref link: https://www.kdnuggets.com/2019/05/animations-with-matplotlib.html
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

if __name__ == '__main__':
    plt.style.use('seaborn-pastel')
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
    line, = ax.plot([], [], lw=3)
    
    def init():
        line.set_data([], [])
        return line,
    def animate(i):
        x = np.linspace(0, 4, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        line.set_data(x, y)
        return line,
    
    anim = FuncAnimation(fig, animate, init_func=init,
                                   frames=200, interval=20, blit=True)
    anim.save('sine_wave.gif', writer='imagemagick')
