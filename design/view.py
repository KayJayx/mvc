from design.designer import Designer
from design.designer import cc
import typing

class UIControl():

    """
    The responsibility of this class is to tie a control which will set off an event
    to a controller class instance.
    """

    def __init__(self, control: cc.Control) -> None:
        self.control  = control
        self.listener = None

    def AttachListener(self, controller: typing.Any) -> None:
        """
        Attach an instance of the controller class that should listen for events from
        this UI Control
        """
        self.listener = controller

class View(Designer):

    """
    The responsibility of the View is to get user input and display data to the user.
    The View is also tightly coupled with the designer class, as it holds the actual
    objects which are displayed to the user. In this case, the View class just holds
    the callback functions for the controls we plan on using.
    """

    def __init__(self) -> None:

        # Create an instance of the base designer class
        super().__init__()

        # Add the user data and callback functions here
        # IDEA: We can create classes that take the control object as input in the constructor
        # and all this class does is tie a controller to the control object, in other words
        # register a listener object
        self.generate_waveform_button.SetButtonCallback(callback=View.GenerateWaveFormButtonCallback)
        self.generate_waveform_button.SetButtonUserData(user_data=self)
        #self.generate_waveform_button.SetButtonUserData(user_data=self.designer.generate_waveform)
        self.stop_waveform_button.SetButtonCallback(callback=View.StopWaveFormButtonCallback)
        self.stop_waveform_button.SetButtonUserData(user_data=self)
        #self.stop_waveform_button.SetButtonUserData(user_data=self.designer.generate_waveform)
        self.clear_plot_button.SetButtonCallback(callback=View.ClearPlotsButtonCallback)
        self.clear_plot_button.SetButtonUserData(user_data=self)
        #self.clear_plot_button.SetButtonUserData(user_data=self.designer.clear_plots)
        self.frequency_slider.SetSliderCallback(callback=View.FrequencySliderCallback)
        self.frequency_slider.SetSliderUserData(user_data=self)
        #self.frequency_slider.SetSliderUserData(user_data=self.designer)

    @property
    def get_frequency(self) -> float:
        """
        Gets the frequency from the slider
        """
        return self.frequency_slider.GetSliderValue()
    
    @property
    def set_angular_frequency(self, angular_frequency: float) -> None:
        """
        Sets the angular frequency to the label
        """
        self.angular_label.SetLabel(f"Angular Freq: {'{:.3f}'.format(angular_frequency)}")

    @property
    def set_period(self, period: float) -> None:
        """
        Sets the period to the label
        """
        self.period_label.SetLabel(f"Period: {'{:.3f}'.format(period)}")

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