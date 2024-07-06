from design.views._designer import cc
import design.controllers.checkbox_controller as cbc

class CheckboxView():

    """
    The responsibility of this class is to take in a checkbox control, tie the control
    with a controller or listener and forward info to the controller or listener.
    """

    def __init__(self, checkbox: cc.CheckBox) -> None:
        self.checkbox   = checkbox
        self.controller = None

        # Set the callback for the checkbox to be this classes method
        self.checkbox.SetCallback(self.OnCheck)

    def AttachController(self, controller: cbc.CheckboxController) -> None:
        """
        Attach a listener controller to the view
        """
        self.controller = controller

    def OnCheck(self) -> None:
        """
        When the user checks the checkbox
        """
        self.controller.OnCheck()

class NormalizeCheckboxView(CheckboxView):

    """
    The view for the normalize checkbox control
    """

    def __init__(self, checkbox: cc.CheckBox) -> None:
        super().__init__(checkbox)