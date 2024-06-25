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