import typing

class LabelModel():

    """
    The responsibility of this class is to hold information about a label.
    """

    def __init__(self) -> None:
        self.value = None

    def SetValue(self, value: typing.Any) -> None:
        """
        Set the value of the label
        """
        self.value = value

    def GetValue(self) -> typing.Any:
        """
        Get the value of the label
        """
        return self.value
    
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