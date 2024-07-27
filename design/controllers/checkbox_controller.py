from __future__ import annotations
import design.models.checkbox_model as cm
import design.views._view as _view

class CheckboxController():

    """
    The responsibility of this class is to act as a bridge between the checkbox model and view classes.
    """

    def __init__(self, checkbox_model: cm.CheckboxModel, view: _view.View) -> None:
        self.checkbox_model = checkbox_model
        self.view           = view

    def OnCheck(self) -> None:
        """
        For when the user checks the checkbox
        """
        pass

class NormalizeCheckboxController(CheckboxController):

    """
    The responsibility of this class is to primarily handle the checkbox checks for the normalize checkbox.
    """

    def __init__(self, checkbox_model: cm.NormalizeCheckboxModel, view: _view.View) -> None:
        super().__init__(checkbox_model, view)
        self.view.norm_checkbox_view.AttachController(controller=self)

    def OnCheck(self) -> None:
        """
        For when the user checks the normalize checkbox
        """
        if self.checkbox_model.IsChecked():
            self.checkbox_model.ClearCheckEvent()
        else:
            self.checkbox_model.SetCheckEvent()