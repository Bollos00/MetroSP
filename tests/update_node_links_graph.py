from scipy.stats import linregress
import numpy
from matplotlib import pyplot, style

from node_link_updater import NodeLinkUpdater

style.use('fivethirtyeight')

def solve(value0, samples, t_end):
    samples = NodeLinkUpdater.sort_samples(samples)
    samples_out_r = NodeLinkUpdater.remove_outliers(samples)
    lr = linregress(samples_out_r)
    result = NodeLinkUpdater.lr_predict(lr, t_end)
    time_x = numpy.linspace(0, t_end, 20)
    
    diff = result - value0
        
    if diff < 0 and diff < -NodeLinkUpdater.MAXIMUM_DIFF:
        diff = -NodeLinkUpdater.MAXIMUM_DIFF
    elif diff > 0 and diff > NodeLinkUpdater.MAXIMUM_DIFF:
        diff = NodeLinkUpdater.MAXIMUM_DIFF

    if samples.shape[0] < NodeLinkUpdater.CONFIDENCE_SAMPLES_COUNT:
        diff *= samples.shape[0]/NodeLinkUpdater.CONFIDENCE_SAMPLES_COUNT

    result = int(value0 + diff + .5)

    
    pyplot.plot(samples[:, 0], samples[:, 1], 'ro', label='outliers')
    pyplot.plot(samples_out_r[:, 0], samples_out_r[:, 1], 'bo', label='amostras')
    pyplot.plot(0, value0, '*c', markersize=22, label=f'tempo ligação inicial ({value0})')
    pyplot.plot(t_end, result, '*m', markersize=22, label=f'tempo ligação final ({result})')
    pyplot.plot(time_x, NodeLinkUpdater.lr_predict(lr, time_x), 'g', label='reta tendência')
    pyplot.plot([0, t_end], [value0, value0], '--', linewidth=.5, color='black')
    pyplot.plot([t_end, t_end], [value0, result], '--', linewidth=.5, color='black')
    pyplot.xlabel('Timestamp (s)')
    pyplot.ylabel('Tempo da ligação (s)')
    pyplot.legend()
    pyplot.grid(True)
    pyplot.show()


if __name__ == "__main__":
    N_SAMPLES = 20
    TIME_NOISE = 20
    VALUE_NOISE = 100
    value0 = 300
    t_end = NodeLinkUpdater.UPDATE_LIMIT_TIME.seconds
    
    expected_value0 = 400
    expcted_value_end = 500
    lr = linregress(
        x=[0, t_end], y=[expected_value0, expcted_value_end]
    )
    time = numpy.linspace(0, t_end, N_SAMPLES)
    values = NodeLinkUpdater.lr_predict(lr, time)
    
    fake_time = numpy.random.normal(time, TIME_NOISE)
    fake_time[fake_time < 0] = 0
    fake_time[fake_time > t_end] = t_end
    fake_values = numpy.random.normal(values, VALUE_NOISE)
    
    fake_samples = numpy.array([[x, y] for x, y in zip(fake_time, fake_values)])
    
    solve(value0, fake_samples, t_end)
    # a, b, c = solve(value0, fake_samples, t_end)
    # pyplot.plot(fake_samples[:, 0], fake_samples[:, 1], 'mo')
    # pyplot.plot(c[:, 0], c[:, 1], 'bo')
    # pyplot.plot(time, _linear_regression_predict(a, b, time), 'g-')
    # pyplot.plot(value0[0], value0[1], 'ro')
    
    # pyplot.show()
    