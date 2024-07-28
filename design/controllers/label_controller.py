from __future__ import annotations
import design.models.label_model as lm
import design.views._view as _view
import numpy as np

class LabelController():

    """
    The responsibility of this class is to act as a bridge between the label model and view classes.
    """

    def __init__(self, label_model: lm.LabelModel, view: _view.View) -> None:
        self.label_model = label_model
        self.view        = view

    def UpdateLabel(self, label: str) -> None:
        """
        For changes to the label
        """
        pass

class AngularLabelController(LabelController):

    """
    The responsibility of this class is to primarily handle the angular label.
    """

    def __init__(self, label_model: lm.AngularLabelModel, view: _view.View) -> None:
        super().__init__(label_model, view)

    def UpdateLabel(self, label: str) -> None:
        """
        For changes to the angular frequency label
        """
        # We are going to update the model and the view here
        self.label_model.SetLabel(label)
        self.view.angular_label_view.SetLabel(label)

class PeriodLabelController(LabelController):

    """
    The responsibility of this class is to primarily handle the period label.
    """

    def __init__(self, label_model: lm.PeriodLabelModel, view: _view.View) -> None:
        super().__init__(label_model, view)

    def UpdateLabel(self, label: str) -> None:
        """
        For changes to the period label
        """
        # We are going to update the model and the view here
        self.label_model.SetLabel(label)
        self.view.period_label_view.SetLabel(label)