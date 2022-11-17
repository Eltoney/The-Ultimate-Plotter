import matplotlib.pyplot as plt
import numpy as np


def my_plotter(min_x, max_x, func, origin_func):
    """
    :params:    min_x: type: float     description: the smallest x value
                max_x: type: float     description: the highest  x value
                func:  type: string    description: f(x) ready to be graphed
                origin_func type:string  description: origin function entered by user

    :return: None

    The function takes the min and max X value and plot the graph for each point in the range
    using the fucntion y = f(x)

    """
    x = np.linspace(min_x, max_x)
    y = eval(func)
    plt.plot(x, y, '-g', label=origin_func)
    plt.title(f'Graph of {origin_func}', color='red')
    plt.xlabel('x', color='blue', fontsize=18)
    plt.ylabel('y', color='brown', fontsize=16)
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
    
