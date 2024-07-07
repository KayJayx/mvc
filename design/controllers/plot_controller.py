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

    def OnChange(self) -> None:
        """
        For when the changes the plot
        """
        pass

class TimePlotController(PlotController):

    """
    The responsibility of this class is to primarily handle the updating of the time plot.
    """

    def __init__(self, plot_model: pm.TimePlotModel, view: _view.View) -> None:
        super().__init__(plot_model, view)

class FrequencyPlotController(PlotController):

    """
    The responsibility of this class is to primarily handle the updating of the frequency plot.
    """

    def __init__(self, plot_model: pm.FrequencyPlotModel, view: _view.View) -> None:
        super().__init__(plot_model, view)