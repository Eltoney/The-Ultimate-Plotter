from validator import (experession_check, bracket_check, function_checker,
                       limits_checker, limit_error_message)


def test_expression_check_1():
    check = experession_check('x + 5 * x + 2')
    assert check == 1


def test_expression_check_2():
    check = experession_check('x + 5 * x + 2 + x ^ 3')
    assert check == 1


def test_expression_check_3():
    check = experession_check('y + 5 * x + 2')
    assert check == 0


def test_expression_check_4():
    check = experession_check('y * 2 + 5')
    assert check == 0


def test_limits_checker_1():
    check = limits_checker(2, 100000)
    assert check == 0


def test_limits_checker_2():
    check = limits_checker(300, 5000)
    assert check == 0


def test_limits_checker3():
    check = limits_checker(100, 100)
    assert check == 1


def test_limits_checker4():
    check = limits_checker(100, 50)
    assert check == 2


def test_limit_error_message1():
    message = limit_error_message(1)
    assert message == 'The lower and upper limits can not be equal'


def test_limit_error_message2():
    message = limit_error_message(2)
    assert message == 'The lower limit can not be higher than upper limit'


def test_bracket_check1():
    assert bracket_check('2 + 5 * (x)') == 1


def test_bracket_check2():
    assert bracket_check('(2 + x) + (5 + x)') == 1


def test_bracket_check3():
    assert bracket_check('(2 + x) + (5 + x') == 0


def test_bracket_check3():
    assert bracket_check('3 * x + () * 5') == 0


def test_function_checker1():
    assert function_checker('5 + 2 * x') == 0


def test_function_checker2():
    assert function_checker('5 * x + 2 * y') == 1


def test_function_checker3():
    assert function_checker('5 + 5 * sin(x)') == 0


def test_function_checker4():
    assert function_checker('5 * x + 2 * ()') == 2


def test_function_checker5():
    assert function_checker('5 * x + 2 * (y)') == 1


def test_function_checker6():
    assert function_checker('5 * y + 3 + ()') == 3


def test_function_checker7():
    assert function_checker('5 * x + 3 * x ^ 2') == 0
