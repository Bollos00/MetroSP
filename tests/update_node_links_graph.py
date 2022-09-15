from scipy import stats
import numpy
from matplotlib import pyplot

def linear_regression_origin_intercept(x, y):
    l = len(x)
    assert l == len(y)
    a = sum(x*y)/sum(x*x)
    return a


def solve(value0, time, values, t_end):
    norm_time = time - value0[0]
    norm_values = values - value0[1]
    a =  linear_regression_origin_intercept(norm_time, norm_values)
    b = value0[1] - a*value0[0]
    return a, b


def linear_regression_predict(lr, x):
    return _linear_regression_predict(lr.slope, lr.intercept, x)


def _linear_regression_predict(a, b, x):
    return b + a*x


if __name__ == "__main__":
    N_SAMPLES = 200
    TIME_NOISE = 100
    VALUE_NOISE = 100
    DISPLACEMENT_VALUE0 = -100
    value0 = (500, 800) # (time, value)
    t_end = 1000
    expcted_value_end = 700
    lr = stats.linregress(
        [value0[0], t_end],
        [value0[1] + DISPLACEMENT_VALUE0, expcted_value_end]
    )
    time = numpy.linspace(value0[0], t_end, N_SAMPLES)
    fake_values = linear_regression_predict(lr, time)
    fake_time = time + (numpy.random.rand(len(time)) - .5)*TIME_NOISE
    fake_values += (numpy.random.rand(len(fake_values)) - .5)*VALUE_NOISE
    pyplot.plot(fake_time, fake_values, 'bo')
    a, b = solve(value0, fake_time, fake_values, t_end)
    pyplot.plot(time, _linear_regression_predict(a, b, time), 'go')
    pyplot.plot(value0[0], value0[1], 'ro')
    
    pyplot.show()