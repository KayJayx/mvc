from design.views._designer import cc
import design.controllers.button_controller as bc

class ButtonView():

    """
    The responsibility of this class is to take in a button control, tie the control
    with a controller or listener and forward info to the controller or listener.
    """

    def __init__(self, button: cc.Button) -> None:
        self.button     = button
        self.controller = None

        # Set the callback for the button to be this classes method
        self.button.SetCallback(self.OnButtonClick)

    def AttachController(self, controller: bc.ButtonController) -> None:
        """
        Attach a listener controller to the view
        """
        self.controller = controller

    def OnButtonClick(self) -> None:
        """
        When the user clicks the button
        """
        self.controller.OnButtonClick()

class GenerateWaveformButtonView(ButtonView):

    """
    The view for the generate waveform button control
    """

    def __init__(self, button: cc.Button) -> None:
        super().__init__(button)

class StopWaveformButtonView(ButtonView):

    """
    The view for the stop waveform button control
    """

    def __init__(self, button: cc.Button) -> None:
        super().__init__(button)

class ClearWaveformButtonView(ButtonView):

    """
    The view for the clear waveform button control
    """

    def __init__(self, button: cc.Button) -> None:
        super().__init__(button)