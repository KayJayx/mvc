from __future__ import annotations
import design.models.slider_model as sm
import design.views._view as _view

class SliderController():

    """
    The responsibility of this class is to act as a bridge between the slider model and view classes.
    """

    def __init__(self, slider_model: sm.SliderModel, view: _view.View) -> None:
        self.slider_model = slider_model
        self.view         = view

    def OnSlide(self) -> None:
        """
        For when the user slides the slider
        """
        pass

class SampleSliderController(SliderController):

    """
    The responsibility of this class is to primarily handle the sliding for the sample slider.
    """

    def __init__(self, slider_model: sm.SampleSliderModel, view: _view.View) -> None:
        super().__init__(slider_model, view)
        self.view.sample_slider_view.AttachController(controller=self)

    def OnSlide(self) -> None:
        """
        Handles the sliding of the sample slider
        """

        # Get the value from the view
        samples = self.view.sample_slider_view.GetSliderValue()

        # Set the value within the model
        self.slider_model.SetValue(samples)