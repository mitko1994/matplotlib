import matplotlib.pyplot as plt

import matplotlib.dates as dates

from datetime import datetime, timedelta

import unittest


class TestGinput(unittest.TestCase):
    """Github issue #7462
    Verify that the output type of each of the points 
    matches the output of the converter function passed in.
    """

     setUp(self):
        """
        Create a date plot before each test
        """
        times = []
        data = []
        for i in range(0, 10):
            times.append(datetime(2016, 1, 1, 0, 0, 0) + timedelta(seconds=i))
            data.append(i)
        plt.plot_date(times, data)

        

    test_default_behaviour_ginput(self):
        """verify that the default behaviour is preserved if there 
        is no converter passed in"""
        x = plt.ginput()
        assert True, type(x[0][0]) == numpy.float64;

    test_to_datetime_ginput(self):
        """verify that the output type for the clicked point is of type datetime"""
        x = plt.ginput(1, 30, True, 1, 3, 2 dates.num2date)
        self.assertTrue(type(dates.num2date(x[0][0])) == datetime)