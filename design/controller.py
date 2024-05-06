from __future__ import annotations
import design.model as model
import design.view as view

class ButtonSwitchController():

    """
    The responsibility of this class is to act a bridge between the button model and view classes.
    """

    def __init__(self, button_model: model.ButtonSwitchModel, button_view: view.ButtonSwitchView) -> None:
        self.button_model = button_model
        self.button_view  = button_view
        self.button_view.AttachController(controller=self)

    def OnButtonClick(self) -> None:
        """
        When the user clicks the button
        """
        self.button_model.SetClickEvent()

class Controller():

    """
    The responsibility of the Controller is to bridge the gap between the Model and View classes.
    The Controller has lots of responsibilities which we'll list below:
    1. Get data from the View (through user input) and pass it to the Model
    2. Get data from the Model and pass it to the View (for displaying)
    """

    def __init__(self) -> None:

        # Create instances of the View and Model classes
        self.view  = view.View()
        self.model = model.Model()

        # Create controllers here
        self.gen_button_controller = ButtonSwitchController(self.model.gen_button_model, self.view.gen_button_view)

        # Run the designer to actually display the info to the screen
        self.view.Run()