import threading

class CheckboxModel():

    """
    The responsibility of this class is to hold state information about a checkbox as
    to whether it was checked or not.
    """

    def __init__(self) -> None:
        self.check_event = threading.Event()

    def IsChecked(self) -> bool:
        """
        Check to see if the checkbox is checked
        """
        return self.check_event.is_set()
    
    def SetCheckEvent(self) -> None:
        """
        Set the check event
        """
        self.check_event.set()
    
    def ClearCheckEvent(self) -> None:
        """
        Clear the check event
        """
        self.check_event.clear()

class NormalizeCheckboxModel(CheckboxModel):

    """
    The responsibility of this class is to hold state information about the normalize checkbox model.
    """

    def __init__(self) -> None:
        super().__init__()