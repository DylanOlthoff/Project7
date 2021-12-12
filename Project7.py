#Dylan Olthoff
# Packages used: numpy, matplotlib
import numpy as np
import matplotlib.pyplot as plt


def lorenz(x, y, z, s=10, r=10, b=8.0 / 3.0):

    x_initial = s * (y - x)  # find the x_dot value
    y_initial = r * x - y - x * z  # find the y_dot value
    z_initial = x * y - b * z  # find the z_dot value
    return x_initial, y_initial, z_initial  # return values


dt = 0.01  # step size
num_steps = 10000  # number of steps
#create empty spaces
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)
ts = np.linspace(0, 100, num_steps + 1)


# Plots
def Graph(si, ri, bi):
    # Set initial values
    xs[0], ys[0], zs[0] = (1., 1.01, 1.02)  # set the initial x, y, z values


    for i in range(num_steps):
        x_initial, y_initial, z_initial = lorenz(xs[i], ys[i], zs[i], s=si, r=ri,
                                     b=bi)  # set the x, y, z values from the lorenz function
        xs[i + 1] = xs[i] + (x_initial * dt)  # input x value into the xspace
        ys[i + 1] = ys[i] + (y_initial * dt)  # input y value into the xspace
        zs[i + 1] = zs[i] + (z_initial * dt)  # input z value into the xspace

    fig = plt.figure(1)  # create the figure to plot the 3d graph
    ax = fig.gca(projection='3d')  # create the 3d graph

    ax.plot(xs, ys, zs, lw=0.5)  # plot the xspace, yspace, and zspace
    ax.set_xlabel("X Axis")  # x axis label
    ax.set_ylabel("Y Axis")  # y axis label
    ax.set_zlabel("Z Axis")  # z axis label
    ax.set_title("Lorenz Graph")  # title label

    plt.show()  # show graph


userInput = int(input(
    "Enter 1 to begin"))  # user input to start code, type 1 to start
while (userInput == 1):  # user input 1 to start
    s = float(input("Input s value: "))  # user input for sigma
    r = float(input("Input r value: "))  # user input for row
    b = float(input("Input b value: "))  # user input for beta

    Graph(s, r, b)  # plot the graph with the user values
    userInput = int(input(
        "Enter 1 to enter new values"))
