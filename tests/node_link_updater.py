import numpy
import datetime
from scipy.stats import linregress
from matplotlib import pyplot


class NodeLinkUpdater:
    INITIAL_DELAY = datetime.timedelta(seconds=5).seconds
    UPDATE_PERIOD = datetime.timedelta(seconds=60)
    UPDATE_LIMIT_TIME = datetime.timedelta(minutes=2, seconds=30)

    OUTLIER_FILTER_N = 1.5
    OUTLIER_FILTER_SAMPLES_PER_SPLIT = 10
    OUTLIER_FILTER_MAX_SPLITS = 4
    
    CONFIDENCE_SAMPLES_COUNT = 20
    MAXIMUM_DIFF = 60
    MINIMUM_UPDATED_TIME = 30

    @classmethod
    def _remove_outfiles_single(cls, s):
        values = s[:, 1]
        avg_values = numpy.average(values)
        std_values = numpy.std(values)
        return s[numpy.abs(s[:, 1] - avg_values) < cls.OUTLIER_FILTER_N*std_values]
        

    @classmethod
    def remove_outliers(cls, samples):
        # quantidade de subamostras
        splits = int(numpy.min([
            1 + samples.shape[0]/cls.OUTLIER_FILTER_SAMPLES_PER_SPLIT,
            cls.OUTLIER_FILTER_MAX_SPLITS
        ]))
        subsamples = numpy.array_split(samples, splits)
        for i, s in enumerate(subsamples):
            subsamples[i] = cls._remove_outfiles_single(s)
        return numpy.vstack(subsamples)


    @classmethod
    def solve(cls, sample0, samples, t_end):
        samples = cls.sort_samples(samples)
        samples = cls.remove_outliers(samples)
        if samples.size == 0:
            return sample0[1]
        
        lr = linregress(samples)
        result = cls.lr_predict(lr, t_end)
        diff = result - sample0[1]
            
        if diff < 0 and diff < -cls.MAXIMUM_DIFF:
            diff = -cls.MAXIMUM_DIFF
        elif diff > 0 and diff > cls.MAXIMUM_DIFF:
            diff = cls.MAXIMUM_DIFF

        if samples.shape[0] < cls.CONFIDENCE_SAMPLES_COUNT:
            diff *= samples.shape[0]/cls.CONFIDENCE_SAMPLES_COUNT

        result = int(sample0[1] + diff + .5)

        return numpy.max([result, cls.MINIMUM_UPDATED_TIME])


    @classmethod
    def lr_predict(cls, lr, x):
        return cls._lr_predict(lr.slope, lr.intercept, x)

    @staticmethod
    def _lr_predict(a, b, x):
        return b + a*x


    @staticmethod
    def sort_samples(samples):
        # Sort array by timestamp (dimensions 0)
        return numpy.array(sorted(samples, key=lambda s: s[0]))
