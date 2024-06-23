import typing

class SliderModel():

    """
    The responsibility of this class is to hold slider information.
    """

    def __init__(self) -> None:
        self.value = None

    def SetValue(self, value: typing.Any) -> None:
        """
        Set the value of the slider
        """
        self.value = value

    def GetValue(self) -> typing.Any:
        """
        Get the value of the slider
        """
        return self.value
    
class SampleSliderModel(SliderModel):

    """
    The responsibility of this class is to hold the sample slider information.
    """

    def __init__(self) -> None:
        super().__init__()