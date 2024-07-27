from __future__ import annotations
from design.views._designer import Designer
import design.views.button_view as bv
import design.views.slider_view as sv
import design.views.label_view as lv
import design.views.checkbox_view as cv
import design.views.plot_view as pv

class View():

    """
    The responsibility of the View is to get user input and display data to the user.
    The View is also tightly coupled with the designer class, as it holds the actual
    objects which are displayed to the user.
    """

    def __init__(self) -> None:
        super().__init__()
        self.designer               = Designer()
        self.gen_button_view        = bv.GenerateWaveformButtonView(self.designer.generate_waveform_button)
        self.stop_button_view       = bv.StopWaveformButtonView(self.designer.stop_waveform_button)
        self.clear_button_view      = bv.ClearWaveformButtonView(self.designer.clear_plot_button)
        self.resolution_slider_view = sv.ResolutionSliderView(self.designer.resolution_slider)
        self.amplitude_slider_view  = sv.AmplitudeSliderView(self.designer.amplitude_slider)
        self.height_slider_view     = sv.HeightSliderView(self.designer.height_slider)
        self.phase_slider_view      = sv.PhaseSliderView(self.designer.phase_slider)
        self.frequency_slider_view  = sv.FrequencySliderView(self.designer.frequency_slider)
        self.angular_label_view     = lv.AngularLabelView(self.designer.angular_label)
        self.period_label_view      = lv.PeriodLabelView(self.designer.period_label)
        self.norm_checkbox_view     = cv.NormalizeCheckboxView(self.designer.normalize_freq)
        self.time_plot_view         = pv.TimePlotView(self.designer.time_plot)
        self.frequency_plot_view    = pv.FrequencyPlotView(self.designer.freq_plot)