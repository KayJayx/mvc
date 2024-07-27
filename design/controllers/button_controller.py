from __future__ import annotations
import design.models.button_model as bm
import design.views._view as _view

class ButtonController():

    """
    The responsibility of this class is to act as a bridge between the button model and view classes.
    """

    def __init__(self, button_model: bm.ButtonModel, view: _view.View) -> None:
        self.button_model = button_model
        self.view         = view

    def OnButtonClick(self) -> None:
        """
        For when the user clicks the button
        """
        self.button_model.SetClickEvent()

class GenerateWaveformButtonController(ButtonController):

    """
    The responsibility of this class is to primarily handle the button presses for the generate
    waveform button.
    """

    def __init__(self, button_model: bm.GenerateWaveformButtonModel, view: _view.View) -> None:
        super().__init__(button_model, view)
        self.view.gen_button_view.AttachController(controller=self)

class ClearWaveformButtonController(ButtonController):

    """
    The responsibility of this class is to primarily handle the button presses for the clear
    waveform button.
    """

    def __init__(self, button_model: bm.ClearWaveformButtonModel, view: _view.View) -> None:
        super().__init__(button_model, view)
        self.view.clear_button_view.AttachController(controller=self)