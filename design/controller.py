from design.view import View
from design.model import Model

class Controller():

    """
    The responsibility of the Controller is to bridge the gap between the Model and View classes.
    The Controller has lots of responsibilities which we'll list below:
    1. Get data from the View (through user input) and pass it to the Model
    2. Get data from the Model and pass it to the View (for displaying)
    """

    def __init__(self) -> None:

        # Create instances of the View and Model classes
        self.view  = View()
        self.model = Model()

        # Run the designer to actually display the info to the screen
        self.view.Run()