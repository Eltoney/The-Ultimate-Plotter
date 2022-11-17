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
    if is_constant_func(func):
        plt.axhline(y, color='g')
        y = np.ones_like(x) * (max_x - min_x + 1)
        # uncomment the line below if you want the label to
        # be the value the constant function evaluate to
        # origin_func = eval(func)

    fig = plt.figure()
    plt.plot(x, y, '-g', label=origin_func)
    plt.title(f'Graph of {origin_func}', color='red')
    plt.xlabel('x', color='blue', fontsize=18)
    plt.ylabel('y', color='brown', fontsize=16)
    plt.legend(loc='upper left')
    plt.grid()
    return fig


def is_constant_func(func):
    """
    :params: func: type:string   description: formated function ready to plot
    :return: bool
    Function takes the maths function, return True if it is a constant function and
    False if it not
    """
    try:
        temp = eval(func)
    except:
        return False
    return True
