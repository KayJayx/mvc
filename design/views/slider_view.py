from design.views._designer import cc
import design.controllers.slider_controller as sc
import typing

class SliderView():

    """
    The responsibility of this class is to take in a slider control, tie the control
    with a controller or listener and forward info to the controller or listener.
    """

    def __init__(self, slider: cc.Slider) -> None:
        self.slider     = slider
        self.controller = None

        # Set the callback for the slider to be this classes method
        self.slider.SetCallback(self.OnSlide)

    def AttachController(self, controller: sc.SliderController) -> None:
        """
        Attach a listener controller to the view
        """
        self.controller = controller

    def OnSlide(self) -> None:
        """
        When the user slides the slider
        """
        self.controller.OnSlide()

    def SetSliderValue(self, value: typing.Any) -> None:
        """
        Set the value of the slider
        """
        self.slider.SetValue(value)

    def GetSliderValue(self) -> typing.Any:
        """
        Get the value of the slider
        """
        return self.slider.GetValue()

class ResolutionSliderView(SliderView):

    """
    The view for the sample slider control
    """

    def __init__(self, slider: cc.Slider) -> None:
        super().__init__(slider)

class AmplitudeSliderView(SliderView):

    """
    The view for the amplitude slider control
    """

    def __init__(self, slider: cc.Slider) -> None:
        super().__init__(slider)

class HeightSliderView(SliderView):

    """
    The view for the height slider control
    """

    def __init__(self, slider: cc.Slider) -> None:
        super().__init__(slider)

class PhaseSliderView(SliderView):

    """
    The view for the phase slider control
    """

    def __init__(self, slider: cc.Slider) -> None:
        super().__init__(slider)

class FrequencySliderView(SliderView):

    """
    The view for the frequency slider control
    """

    def __init__(self, slider: cc.Slider) -> None:
        super().__init__(slider)