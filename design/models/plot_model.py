import typing

class PlotModel():

    """
    The responsibility of this class is to hold information about a plot.
    """

    def __init__(self) -> None:
        self.plot_data = None

    def SetPlotData(self, plot_data: typing.Any) -> None:
        """
        Set the plot data
        """
        pass

    def GetPlotData(self) -> typing.Any:
        """
        Get the plot data
        """
        pass

class TimePlotModel(PlotModel):

    """
    The responsibility of this class is to hold the time plot information.
    """

    def __init__(self) -> None:
        super().__init__()