import typing
import threading

class SliderModel():

    """
    The responsibility of this class is to hold slider information.
    """

    def __init__(self) -> None:
        self.value = None
        self.lock  = threading.Lock()

    def SetValue(self, value: typing.Any) -> None:
        """
        Set the value of the slider
        """
        with self.lock:
            self.value = value

    def GetValue(self) -> typing.Any:
        """
        Get the value of the slider
        """
        with self.lock:
            return self.value
    
class ResolutionSliderModel(SliderModel):

    """
    The responsibility of this class is to hold the sample slider information.
    """

    def __init__(self) -> None:
        super().__init__()

class AmplitudeSliderModel(SliderModel):

    """
    The responsibility of this class is to hold the amplitude slider information.
    """

    def __init__(self) -> None:
        super().__init__()

class HeightSliderModel(SliderModel):

    """
    The responsibility of this class is to hold the height slider information.
    """

    def __init__(self) -> None:
        super().__init__()

class PhaseSliderModel(SliderModel):

    """
    The responsibility of this class is to hold the phase slider information.
    """

    def __init__(self) -> None:
        super().__init__()

class FrequencySliderModel(SliderModel):

    """
    The responsibility of this class is to hold the frequency slider information.
    """

    def __init__(self) -> None:
        super().__init__()