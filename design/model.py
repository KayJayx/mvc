from __future__ import annotations
import threading

class ButtonSwitchModel():

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

class Model():

    """
    The responsibility of the Model is to hold state information related to the application.
    It should have no concept of what is going on in the outside world, relative to the
    view and controller classes.
    """

    def __init__(self) -> None:

        # Create models here
        self.gen_button_model = ButtonSwitchModel()