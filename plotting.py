import matplotlib.pyplot as plt
import numpy as np


def function_format(func):
    """
    :param  func: type:str      description: mathematical function typed by the user
    :return func: type:Str      description: formatted expression by adding python terms instead of raw math terms.

    Function format the func string to prepare it for plotting.
    """

    supported_expression = {
        '^': '**',
        'sin': 'np.sin',
        'cos': 'np.cos',
        'tan': 'np.tan'
    }
    for term in supported_expression.keys():
        func = func.replace(term, supported_expression[term])
    return func.replace(' ', '')


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


def plot_prepare(min_x, max_x, func):
    """
    :params:    min_x: type: float     description: the smallest x value
                max_x: type: float     description: the highest  x value
                func:  type: string    description: f(x) ready to be graphed
                origin_func type:string  description: origin function entered by user
    :return: tuple contains (x , y)
    The function takes the min and max X value and the function and return x,y as numpy arrays to 
    be plotted.
    """
    x = np.linspace(min_x, max_x)
    if is_constant_func(func):
        y = np.ones_like(x) * (max_x - min_x + 1)
    else:
        y = eval(function_format(func))
    return (x, y)
