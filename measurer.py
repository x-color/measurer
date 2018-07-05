import sys
import time


class Measurer:
    """
    This class is measuring run time of a function.

    How to use...
        >>> measurer = Measurer()
        >>> measurer.measure(function)
    """

    def __init__(self, repeat=100, color=True):
        """
        Argument:
            repeat (int): The number of executions of measured a function.
                          This number must be larger than 1.
            color (boolean): Coloring log messge.
        """
        if repeat < 1:
            raise('Please set repeat >= 1')
        self.repeat = int(repeat)
        self.color = color

    def measure(self, function, *args):
        """
        Measure run time of a function and display log message.

        Arguments:
            function (function): It is a function you want to measure.
            args (tuple): This argument is passed to measured a funstion.

        Return:
            result (string): Message of result of measuring a function.
        """
        start_message = self._message('\033[33m') + '\r'
        sys.stdout.write(start_message.format(' Running ', function.__name__))
        sys.stdout.flush()
        elapsed_time, average_time = self._measure(function, args)
        finish_message = self._message('\033[32m')
        print(finish_message.format('Completed', function.__name__))
        print("    Total  : {}[sec]".format(elapsed_time))
        print("    Average: {}[sec]".format(average_time))
        result = '{},{},{}'.format(function.__name__, elapsed_time, average_time)
        return result

    def _measure(self, function, args):
        """
        Measure run time of a function.

        Arguments:
            function (function): It is a function you want to measure.
            args (tuple): This argument is passed to measured a funstion.

        Returns:
            elapsed_time (float): Total run time of a function.
            average_time (float): Average run time of a function.
        """
        start = time.time()
        for t in range(self.repeat):
            function(*args)
        elapsed_time = time.time() - start
        average_time = elapsed_time / self.repeat
        return elapsed_time, average_time

    def _message(self, color_code):
        """
        Generate start and finish message.

        Arguments:
            color_code (string): Color code.

        Returns:
            message (string): Start or finish message.
        """
        if self.color:
            message = '\033[1m[' + color_code + '{}\033[00m\033[1m] ' \
                            + color_code + '{}()\033[00m'
        else:
            message = '[{}] {}()'
        return message
