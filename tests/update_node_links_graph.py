from scipy import stats
import numpy
from matplotlib import pyplot

def _remove_outfiles_single(s):
    N = 1
    values = s[:, 1]
    avg_values = numpy.average(values)
    std_values = numpy.std(values)
    return s[numpy.abs(s[:, 1] - avg_values) < N*std_values]

def remove_outliers(samples):
    # no máximo 4 splitadas
    splits = int(numpy.min([samples.shape[0]/50 + 1, 4]))
    samples_splited = numpy.array_split(samples, splits)
    for i, s in enumerate(samples_splited):
        samples_splited[i] = _remove_outfiles_single(s)
    return numpy.vstack(samples_splited)

def linear_regression_origin_intercept(samples):
    # Retorna o coefieciente da regressão linear que passa pela origem
    x = samples[:, 0]
    y = samples[:, 1]
    return numpy.sum(x*y)/numpy.sum(x*x)


def linear_regression_point_intercept(sample0, samples):
    # Retorna os coefiecientes da regressão linear que passa por sample0
    norm_samples = samples - sample0
    a = linear_regression_origin_intercept(norm_samples)
    a *= numpy.min([samples.shape[0]/20, 1])
    b = sample0[1] - a*sample0[0]
    return a, b


def solve(sample0, samples, t_end):
    samples = remove_outliers(samples)
    # sample0 é o par de coordenadas da predição anterior (em t=t0)
    # As amostras são normalizados para plotar uma reta que passa
    #  por sample0 
    a, b = linear_regression_point_intercept(sample0, samples)
    return a, b, samples
    # return _linear_regression_predict(a, b, t_end)

def linear_regression_predict(lr, x):
    return _linear_regression_predict(lr.slope, lr.intercept, x)


def _linear_regression_predict(a, b, x):
    return b + a*x


def sort_samples(samples):
    # Sort array by time (dimensions 0)
    return numpy.array(sorted(samples, key=lambda s: s[0]))

if __name__ == "__main__":
    N_SAMPLES = 20
    TIME_NOISE = 200
    VALUE_NOISE = 200
    DISPLACEMENT_VALUE0 = 0
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
    fake_samples = numpy.array([[x, y] for x, y in zip(fake_time, fake_values)])
    fake_samples = sort_samples(fake_samples)

    # pyplot.boxplot(fake_samples[1])
    # pyplot.show()
    
    a, b, c = solve(value0, fake_samples, t_end)
    pyplot.plot(fake_samples[:, 0], fake_samples[:, 1], 'mo')
    pyplot.plot(c[:, 0], c[:, 1], 'bo')
    pyplot.plot(time, _linear_regression_predict(a, b, time), 'g-')
    pyplot.plot(value0[0], value0[1], 'ro')
    
    pyplot.show()
    