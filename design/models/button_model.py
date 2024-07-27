import threading

class ButtonModel():

    """
    The responsibility of this class is to hold state information about a button as
    to whether it was clicked or not.
    """

    def __init__(self) -> None:
        self.click_event = threading.Event()

    def WasClicked(self) -> bool:
        """
        Check to see if the button was previously clicked
        """
        return self.click_event.is_set()
    
    def SetClickEvent(self) -> None:
        """
        Set the click event
        """
        self.click_event.set()
    
    def ClearClickEvent(self) -> None:
        """
        Clear the click event
        """
        self.click_event.clear()

class GenerateWaveformButtonModel(ButtonModel):

    """
    The responsibility of this class is to hold state information about the generate waveform button.
    """

    def __init__(self) -> None:
        super().__init__()

class ClearWaveformButtonModel(ButtonModel):

    """
    The responsibility of this class is to hold state information about the clear waveform button.
    """

    def __init__(self) -> None:
        super().__init__()