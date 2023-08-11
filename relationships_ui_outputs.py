"""
Purpose: Display output for relationships dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""
from shiny import ui
from shinywidgets import output_widget


def get_relationships_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Relationships: Charts"),
            output_widget("relationships_output_widget1"),
            ui.tags.hr(),
        ),
    )
