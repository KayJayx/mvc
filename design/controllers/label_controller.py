from __future__ import annotations
import design.models.label_model as lm
import design.views._view as _view

class LabelController():

    """
    The responsibility of this class is to act as a bridge between the label model and view classes.
    """

    def __init__(self, label_model: lm.LabelModel, view: _view.View) -> None:
        self.label_model = label_model
        self.view        = view

    def OnChange(self) -> None:
        """
        For when the changes the label
        """
        pass

class AngularLabelController(LabelController):

    """
    The responsibility of this class is to primarily handle the angular label.
    """

    def __init__(self, label_model: lm.AngularLabelModel, view: _view.View) -> None:
        super().__init__(label_model, view)

class PeriodLabelController(LabelController):

    """
    The responsibility of this class is to primarily handle the period label.
    """

    def __init__(self, label_model: lm.PeriodLabelModel, view: _view.View) -> None:
        super().__init__(label_model, view)