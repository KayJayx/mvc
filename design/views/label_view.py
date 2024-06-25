from design.views._designer import cc
import design.controllers.label_controller as lc

class LabelView():

    """
    The responsibility of this class is to take in a label control, tie the control
    with a controller or listener and forward info to the controller or listener.
    """

    def __init__(self, label: cc.Label) -> None:
        self.label      = label
        self.controller = None

    def AttachController(self, controller: lc.LabelController) -> None:
        """
        Attach a listener controller to the view
        """
        self.controller = controller

    def SetLabel(self, label: str) -> None:
        """
        Set the label
        """
        self.label.SetValue(label)

    def GetLabel(self) -> str:
        """
        Get the label
        """
        return self.label.GetValue()