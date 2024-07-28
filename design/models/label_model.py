import threading

class LabelModel():

    """
    The responsibility of this class is to hold information about a label.
    """

    def __init__(self) -> None:
        self.label = None
        self.lock  = threading.Lock()

    def SetLabel(self, label: str) -> None:
        """
        Set the value of the label
        """
        with self.lock:
            self.label = label
    
class AngularLabelModel(LabelModel):

    """
    The responsibility of this class is to hold the angular label information.
    """

    def __init__(self) -> None:
        super().__init__()

class PeriodLabelModel(LabelModel):

    """
    The responsibility of this class is to hold the period label information.
    """

    def __init__(self) -> None:
        super().__init__()