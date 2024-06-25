from __future__ import annotations
from design.views._designer import Designer
import design.views.button_view as bv
import design.views.slider_view as sv
import typing

class View():

    """
    The responsibility of the View is to get user input and display data to the user.
    The View is also tightly coupled with the designer class, as it holds the actual
    objects which are displayed to the user.
    """

    def __init__(self) -> None:
        super().__init__()
        self.designer               = Designer()
        self.gen_button_view        = bv.GenerateWaveformButtonView(self.designer.generate_waveform_button)
        self.resolution_slider_view = sv.ResolutionSliderView(self.designer.resolution_slider)
        self.amplitude_slider_view  = sv.AmplitudeSliderView(self.designer.amplitude_slider)

    @property
    def get_frequency(self) -> float:
        """
        Gets the frequency from the slider
        """
        return self.designer.frequency_slider.GetValue()
    
    @property
    def set_angular_frequency(self, angular_frequency: float) -> None:
        """
        Sets the angular frequency to the label
        """
        self.designer.angular_label.SetValue(f"Angular Freq: {'{:.3f}'.format(angular_frequency)}")

    @property
    def set_period(self, period: float) -> None:
        """
        Sets the period to the label
        """
        self.designer.period_label.SetValue(f"Period: {'{:.3f}'.format(period)}")

    @staticmethod
    def GenerateWaveFormButtonCallback(sender: typing.Any, app: typing.Any, user: typing.Any) -> None:
        """
        The callback function that gets called when the button is pushed
        """
        pass

    @staticmethod
    def StopWaveFormButtonCallback(sender: typing.Any, app: typing.Any, user: typing.Any) -> None:
        """
        The callback function that gets called when the button is pushed
        """
        pass

    @staticmethod
    def ClearPlotsButtonCallback(sender: typing.Any, app: typing.Any, user: typing.Any) -> None:
        """
        The callback function that gets called when the button is pushed
        """
        pass

    @staticmethod
    def FrequencySliderCallback(sender: typing.Any, app: typing.Any, user: typing.Any) -> None:
        """
        The callback function that gets called when the slider is moved
        """
        pass
        """
        self.frequency_slider.SetSliderCallback(
            callback=lambda sender, app, user : (
                self.angular_label.SetLabel(f"Angular Freq: {'{:.3f}'.format(2 * np.pi * self.frequency_slider.GetSliderValue())}"),
                self.period_label.SetLabel(f"Period: {'{:.3f}'.format(1 / self.frequency_slider.GetSliderValue())}")
            )
        )
        """