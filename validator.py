def limits_checker(min_x, max_x):
    """
    :params:    min_x: type: float     description: the smallest x value
                max_x: type: float     description: the highest  x value

    :return:    type: int description: error_code 

    The function check for possible errors involving the limits of x and  
    returns a number based on the status 
        0 => no error
        1 => equality of upper and lower limits
        2 => lower limit is higher than upper limit
    """
    if min_x == max_x:
        return 1
    elif min_x > max_x:
        return 2
    return 0


def limit_error_message(check_code):
    """
    :params:    check_code: type: int   description: limits code error

    :return:    type: string  description: error message

    The function takes the error code and returns error message depending on the number
    """
    if check_code == 1:
        return 'The lower and upper limits can not be equal'
    elif check_code == 2:
        return 'The lower limit can not be higher than upper limit'


def experession_check(func):
    """
    :param: func: type: string      description: math expression enterd by user
    :return:    0 if no error found
                1 if there are any error

    Function check that the user used only supported terms and any other term is a number         
    """
    supported = ['*', '/', '-', '+', 'x', '^', 'sin', 'cos', 'tan']
    filtered = func
    filtered = filtered.replace(' ', '')
    for expression in supported:
        filtered = filtered.replace(expression, ' ')
    filtered = filtered.replace('(', '')
    filtered = filtered.replace(')', '')

    terms = filtered.split()
    for term in terms:
        if not term.isnumeric():
            return 0
    return 1


def bracket_check(func):
    """
    :param: func: type: string      description: math expression enterd by user
    :return:    0 if no error found
                1 if there are any error

    Function check that only allowed brackets are used and 
        the bracket format and use are in the correct way
    """
    unsupported_brackets = ['{', '}', '[', ']']
    for bracket in unsupported_brackets:
        if func.find(bracket) != -1:
            return 0
    filtered = func.replace(' ', '')
    for i in range(1, len(filtered)):
        if filtered[i - 1] == '(' and filtered[i] == ')':
            return 0
    bracket_stack = 0
    for term in filtered:
        if term == '(':
            bracket_stack += 1
        elif term == ')':
            if bracket_stack == 0:
                return 0
            else:
                bracket_stack -= 1
    return bracket_stack == 0


def function_checker(func):
    """
    :param  func: type:str      description: mathematical function typed by the user
    :return mask: type:int      description: a number illustrates the error types

    Function take mathematical function as string and valdiate it
    return: 0: if no error
            1: unsupported terms are used
            2: unsupported brackets format
            3: both unsupported brackets and terms
    """
    mask = 0
    if not experession_check(func):
        mask |= 1
    if not bracket_check(func):
        mask |= 2
    return mask


def function_error_message(check_code):
    """
    :param: check_code: type:int    description: error code from valdiation function
    :return error_list: type:list   description: list contain error messages based on error code

    Function takes error code mask and return the messages that illustrates what have gone wrong
    """
    error_list = []
    if (check_code & 1) == 1:
        error_list.append('Using unsupported terms')
    if ((check_code >> 1) & 1) == 1:
        error_list.append('Using unsupported brackets format')
    return error_list

def request_graph(min_x, max_x, func):
    """
    :params:    min_x: type: float     description: the smallest x value
                max_x: type: float     description: the highest  x value
                func:  type: string    description: math function entered by user

    :return
            a figure of the plotted graph if no errors found
            else
            errors type: list   description: error message list

    Function that check if any errors in the expression are found and report the errors,
    if no errors found it send the expression and limit to the plotting function to plot it
    then return the figure.
    """
    limit_error_code = limits_checker(min_x, max_x)
    func_error_code = function_checker(func)

    if limit_error_code + func_error_code == 0:
        return []
    else:
        errors = function_error_message(func_error_code)
        limt_errors = limit_error_message(limit_error_code)
        if limt_errors != None:
            errors.append(limt_errors)
        return errors
