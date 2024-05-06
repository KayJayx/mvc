from __future__ import annotations
from design.designer import Designer
from design.designer import cc
import design.controller as controller
import typing

class ButtonSwitchView():

    """
    The responsibility of this class is to take in a button control, tie the control
    with a controller or listener and forward info to the controller or listener.
    """

    def __init__(self, button: cc.Button) -> None:
        self.button     = button
        self.controller = None

        # Set the callback for the button to be this classes method
        self.button.SetCallback(self.OnButtonClick)

    def AttachController(self, controller: controller.ButtonSwitchController) -> None:
        """
        Attach a listener controller to the view
        """
        self.controller = controller

    def OnButtonClick(self) -> None:
        """
        When the user clicks the button
        """
        self.controller.OnButtonClick()

class View(Designer):

    """
    The responsibility of the View is to get user input and display data to the user.
    The View is also tightly coupled with the designer class, as it holds the actual
    objects which are displayed to the user.
    """

    def __init__(self) -> None:

        # Create an instance of the base designer class
        super().__init__()

        # Create views here
        self.gen_button_view = ButtonSwitchView(button=self.generate_waveform_button)

    @property
    def get_frequency(self) -> float:
        """
        Gets the frequency from the slider
        """
        return self.frequency_slider.GetValue()
    
    @property
    def set_angular_frequency(self, angular_frequency: float) -> None:
        """
        Sets the angular frequency to the label
        """
        self.angular_label.SetValue(f"Angular Freq: {'{:.3f}'.format(angular_frequency)}")

    @property
    def set_period(self, period: float) -> None:
        """
        Sets the period to the label
        """
        self.period_label.SetValue(f"Period: {'{:.3f}'.format(period)}")

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