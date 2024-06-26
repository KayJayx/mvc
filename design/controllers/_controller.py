from __future__ import annotations
import design.views._view as _view
import design.controllers.button_controller as bc
import design.models.button_model as bm
import design.controllers.slider_controller as sc
import design.models.slider_model as sm

class Controller():

    """
    The responsibility of the Controller is to bridge the gap between the Model and View classes.
    The Controller has lots of responsibilities which we'll list below:
    1. Get data from the View (through user input) and pass it to the Model
    2. Get data from the Model and pass it to the View (for displaying)
    """

    def __init__(self) -> None:

        # Create an instance of the View class, the idea is to share the entire view with all of the
        # controller classes such that individual controller subclasses can have the ability to
        # interact with the view
        self.view = _view.View()

        # Create models here
        self.gen_button_model        = bm.GenerateWaveformButtonModel()
        self.resolution_slider_model = sm.ResolutionSliderModel()
        self.amplitude_slider_model  = sm.AmplitudeSliderModel()
        self.height_slider_model     = sm.HeightSliderModel()
        self.phase_slider_model      = sm.PhaseSliderModel()
        self.frequency_slider_model  = sm.FrequencySliderModel()

        # Create controllers here
        self.gen_button_controller        = bc.GenerateWaveformButtonController(self.gen_button_model, self.view)
        self.resolution_slider_controller = sc.ResolutionSliderController(self.resolution_slider_model, self.view)
        self.amplitude_slider_controller  = sc.AmplitudeSliderController(self.amplitude_slider_model, self.view)
        self.height_slider_controller     = sc.HeightSliderController(self.height_slider_model, self.view)
        self.phase_slider_controller      = sc.PhaseSliderController(self.phase_slider_model, self.view)
        self.frequency_slider_controller  = sc.FrequencySliderController(self.frequency_slider_model, self.view)

        # Run the designer to actually display the info to the screen
        self.view.designer.Run()

    def UpdateWaveform(self) -> None:
        """
        The purpose of this function is to update the waveform plot onto the main window
        """
        pass