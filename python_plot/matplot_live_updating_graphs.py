##
# Live updating graphs come in handy when plotting dynamic quantities like stock data, 
# sensor data or any other time-dependent data. 
# We plot a base graph which automatically gets updated as more data is fed 
# into the system. Let’s plot stock prices of a hypothetical company in a month.

#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = open('stock.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []
   
    for line in lines:
        x, y = line.split(',') # Delimiter is comma    
        xs.append(float(x))
        ys.append(float(y))
   
    
    ax1.clear()
    ax1.plot(xs, ys)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Live graph with matplotlib') 
    
    
ani = animation.FuncAnimation(fig, animate, interval=1000) 
plt.show()
