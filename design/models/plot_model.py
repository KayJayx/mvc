import threading

class PlotModel():

    """
    The responsibility of this class is to hold information about a plot.
    """

    def __init__(self) -> None:
        self.x_data = None
        self.y_data = None
        self.lock   = threading.Lock()

    def SetPlotData(self, x_data: list, y_data: list) -> None:
        """
        Set the plot data
        """
        with self.lock:
            self.x_data = x_data
            self.y_data = y_data

class TimePlotModel(PlotModel):

    """
    The responsibility of this class is to hold the time plot information.
    """

    def __init__(self) -> None:
        super().__init__()

class FrequencyPlotModel(PlotModel):

    """
    The responsibility of this class is to hold the frequency plot information.
    """

    def __init__(self) -> None:
        super().__init__()