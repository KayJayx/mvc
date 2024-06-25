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

class ResolutionSliderController(SliderController):

    """
    The responsibility of this class is to primarily handle the sliding for the sample slider.
    """

    def __init__(self, slider_model: sm.ResolutionSliderModel, view: _view.View) -> None:
        super().__init__(slider_model, view)
        self.view.resolution_slider_view.AttachController(controller=self)

    def OnSlide(self) -> None:
        """
        Handles the sliding of the sample slider
        """
        pass

class AmplitudeSliderController(SliderController):

    """
    The responsibility of this class is to primarily handle the sliding for the amplitude slider.
    """

    def __init__(self, slider_model: sm.AmplitudeSliderModel, view: _view.View) -> None:
        super().__init__(slider_model, view)
        self.view.amplitude_slider_view.AttachController(controller=self)

    def OnSlide(self) -> None:
        """
        Handles the sliding of the amplitude slider
        """
        pass

class HeightSliderController(SliderController):

    """
    The responsibility of this class is to primarily handle the sliding for the height slider.
    """

    def __init__(self, slider_model: sm.HeightSliderModel, view: _view.View) -> None:
        super().__init__(slider_model, view)
        self.view.height_slider_view.AttachController(controller=self)

    def OnSlide(self) -> None:
        """
        Handles the sliding of the height slider
        """
        pass

class PhaseSliderController(SliderController):

    """
    The responsibility of this class is to primarily handle the sliding for the phase slider.
    """

    def __init__(self, slider_model: sm.PhaseSliderModel, view: _view.View) -> None:
        super().__init__(slider_model, view)
        self.view.phase_slider_view.AttachController(controller=self)

    def OnSlide(self) -> None:
        """
        Handles the sliding of the phase slider
        """
        pass

class FrequencySliderController(SliderController):

    """
    The responsibility of this class is to primarily handle the sliding for the frequency slider.
    """

    def __init__(self, slider_model: sm.FrequencySliderModel, view: _view.View) -> None:
        super().__init__(slider_model, view)
        self.view.frequency_slider_view.AttachController(controller=self)

    def OnSlide(self) -> None:
        """
        Handles the sliding of the frequency slider
        """
        pass