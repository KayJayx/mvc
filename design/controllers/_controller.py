from __future__ import annotations
import design.views._view as _view
import design.controllers.button_controller as bc
import design.models.button_model as bm
import design.controllers.slider_controller as sc
import design.models.slider_model as sm
import design.controllers.label_controller as lc
import design.models.label_model as lm
import design.controllers.checkbox_controller as cbc
import design.models.checkbox_model as cm
import design.controllers.plot_controller as pc
import design.models.plot_model as pm
import numpy as np

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
        self.clear_button_model      = bm.ClearWaveformButtonModel()
        self.resolution_slider_model = sm.ResolutionSliderModel()
        self.amplitude_slider_model  = sm.AmplitudeSliderModel()
        self.height_slider_model     = sm.HeightSliderModel()
        self.phase_slider_model      = sm.PhaseSliderModel()
        self.frequency_slider_model  = sm.FrequencySliderModel()
        self.angular_label_model     = lm.AngularLabelModel()
        self.period_label_model      = lm.PeriodLabelModel()
        self.norm_checkbox_model     = cm.NormalizeCheckboxModel()
        self.time_plot_model         = pm.TimePlotModel()
        self.frequency_plot_model    = pm.FrequencyPlotModel()

        # Create controllers here
        self.gen_button_controller        = bc.GenerateWaveformButtonController(self.gen_button_model, self.view)
        self.clear_button_controller      = bc.ClearWaveformButtonController(self.clear_button_model, self.view)
        self.resolution_slider_controller = sc.ResolutionSliderController(self.resolution_slider_model, self.view)
        self.amplitude_slider_controller  = sc.AmplitudeSliderController(self.amplitude_slider_model, self.view)
        self.height_slider_controller     = sc.HeightSliderController(self.height_slider_model, self.view)
        self.phase_slider_controller      = sc.PhaseSliderController(self.phase_slider_model, self.view)
        self.frequency_slider_controller  = sc.FrequencySliderController(self.frequency_slider_model, self.view)
        self.angular_label_controller     = lc.AngularLabelController(self.angular_label_model, self.view)
        self.period_label_controller      = lc.PeriodLabelController(self.period_label_model, self.view)
        self.norm_checkbox_controller     = cbc.NormalizeCheckboxController(self.norm_checkbox_model, self.view)
        self.time_plot_controller         = pc.TimePlotController(self.time_plot_model, self.view)
        self.frequency_plot_controller    = pc.FrequencyPlotController(self.frequency_plot_model, self.view)

        # Run the designer to actually display the info to the screen
        self.view.designer.Run(self.UpdateWaveform)

    def UpdateWaveform(self) -> None:
        """
        The purpose of this function is to update the waveform plot onto the main window
        """

        if self.clear_button_controller.button_model.WasClicked():

            self.time_plot_controller.UpdatePlot(x_data=[0], y_data=[0])
            self.clear_button_controller.button_model.ClearClickEvent()
            self.gen_button_controller.button_model.ClearClickEvent()

        if self.gen_button_controller.button_model.WasClicked():
            
            # Get all of the needed information needed to update the plot
            samples   = self.resolution_slider_controller.slider_model.GetValue()
            x_data    = np.linspace(0, self.view.designer.length_of_plot, samples, endpoint=True)
            amplitude = self.amplitude_slider_controller.slider_model.GetValue()
            height    = self.height_slider_controller.slider_model.GetValue()
            phase     = self.phase_slider_controller.slider_model.GetValue()
            frequency = self.frequency_slider_controller.slider_model.GetValue()

            if self.norm_checkbox_controller.checkbox_model.IsChecked():
                y_data = [(amplitude * np.sin(((2 * np.pi * frequency * x) / samples) + phase)) + height for x in x_data]
            else:
                # Digital representation of what would be an analog signal, where samples represents the
                # total number of inputs into my function
                y_data = [(amplitude * np.sin(((2 * np.pi * frequency * x)) + phase)) + height for x in x_data]

            # Plot the data
            self.time_plot_controller.UpdatePlot(x_data=x_data, y_data=y_data)

            # Update the labels with new data
            self.angular_label_controller.UpdateLabel(f"Angular Freq: {'{:.3f}'.format(2 * np.pi * self.frequency_slider_controller.slider_model.GetValue())}")
            self.period_label_controller.UpdateLabel(f"Period: {'{:.3f}'.format(1 / self.frequency_slider_controller.slider_model.GetValue())}")