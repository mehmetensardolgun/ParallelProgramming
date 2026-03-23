import inspect

custom_power = lambda x=0, /, e=1: x**e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the mathematical equation (x**a + y**b) / c.

    :param x: The first base value (positional-only).
    :type x: int
    :param y: The second base value (positional-only).
    :type y: int
    :param a: The exponent for x (positional-or-keyword).
    :type a: int
    :param b: The exponent for y (positional-or-keyword).
    :type b: int
    :param c: The divisor (keyword-only).
    :type c: int
    :return: The result of the equation.
    :rtype: float
    """
    return float((x**a + y**b) / c)


def fn_w_counter() -> tuple[int, dict[str, int]]:
    
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.caller_info = {}

    fn_w_counter.total_calls += 1

    caller_frame = inspect.currentframe().f_back
    caller_name = caller_frame.f_globals.get('__name__', 'unknown')

    fn_w_counter.caller_info[caller_name] = fn_w_counter.caller_info.get(caller_name, 0) + 1

    return fn_w_counter.total_calls, fn_w_counter.caller_info.copy()
