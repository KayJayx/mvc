from __future__ import annotations
import design.models.plot_model as pm
import design.views._view as _view

class PlotController():

    """
    The responsibility of this class is to act as a bridge between the plot model and view classes.
    """

    def __init__(self, plot_model: pm.PlotModel, view: _view.View) -> None:
        self.plot_model = plot_model
        self.view       = view

    def UpdatePlot(self, x_data: list, y_data: list) -> None:
        """
        Called when updating the plot
        """
        pass

class TimePlotController(PlotController):

    """
    The responsibility of this class is to primarily handle the updating of the time plot.
    """

    def __init__(self, plot_model: pm.TimePlotModel, view: _view.View) -> None:
        super().__init__(plot_model, view)

    def UpdatePlot(self, x_data: list, y_data: list) -> None:
        """
        For when the time plot needs to be updated
        """
        # We are going to update the model and the view here
        self.plot_model.SetPlotData(x_data=x_data, y_data=y_data)
        self.view.time_plot_view.SetPlotData(x_data=x_data, y_data=y_data)

class FrequencyPlotController(PlotController):

    """
    The responsibility of this class is to primarily handle the updating of the frequency plot.
    """

    def __init__(self, plot_model: pm.FrequencyPlotModel, view: _view.View) -> None:
        super().__init__(plot_model, view)

    def UpdatePlot(self, x_data: list, y_data: list) -> None:
        """
        For when the frequency plot needs to be updated
        """
        # We are going to update the model and the view here
        self.plot_model.SetPlotData(x_data=x_data, y_data=y_data)
        self.view.frequency_plot_view.SetPlotData(x_data=x_data, y_data=y_data)