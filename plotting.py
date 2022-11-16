import matplotlib.pyplot as plt
import numpy as np


def my_plotter(min_x, max_x, func):
    """
    :params:    min_x: type: float     description: the smallest x value
                max_x: type: float     description: the highest  x value
                func:  type: string    description: f(x) of each x value in the range

    :return: None

    The function takes the min and max X value and plot the graph for each point in the range
    using the fucntion y = f(x)

    """
    x = np.linspace(min_x, max_x)
    y = eval(func)
    plt.plot(x, y, '-g', label=func)
    plt.title(f'Graph of {func}', color='red')
    plt.xlabel('x', color='blue')
    plt.ylabel('y', color='brown')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

