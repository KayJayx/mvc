from design.views._designer import cc
import design.controllers.plot_controller as pc

class PlotView():

    """
    The responsibility of this class is to take in a plot control, tie the control
    with a controller or listener and forward info to the controller or listener.
    """

    def __init__(self, plot: cc.Plot) -> None:
        self.plot       = plot
        self.controller = None

    def AttachController(self, controller: pc.PlotController) -> None:
        """
        Attach a listener controller to the view
        """
        self.controller = controller

    def SetPlotData(self, x_data: list, y_data: list) -> None:
        """
        Set the plot data
        """
        self.plot.PlotLineSeriesData(x_data=x_data, y_data=y_data)

class TimePlotView(PlotView):

    """
    The view for the time plot control
    """

    def __init__(self, plot: cc.Plot) -> None:
        super().__init__(plot)

class FrequencyPlotView(PlotView):

    """
    The view for the frequency plot control
    """

    def __init__(self, plot: cc.Plot) -> None:
        super().__init__(plot)