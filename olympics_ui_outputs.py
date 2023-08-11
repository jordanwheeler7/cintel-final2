"""
Purpose: Display output for MT Cars dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""
from shiny import ui
from shinywidgets import output_widget


def get_summer_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Filtered Olympics: Charts"),
            output_widget("summer_output_widget1"),
            ui.output_plot("summer_plot1"),
            ui.output_plot("summer_plot2"),
            output_widget("summer_plot3"),
            ui.tags.hr(),
            ui.h3("Filtered Summer Table"),
            ui.output_text("summer_record_count_string"),
            ui.output_table("summer_filtered_table"),
            ui.tags.hr(),
        ),
    )
