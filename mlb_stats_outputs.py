"""
Purpose: Display output for Mlb Stats dataset.

@imports shiny.ui as ui
@imports shinywidgets.output_widget for interactive charts
"""
from shiny import ui
from shinywidgets import output_widget


def get_baseball_data_outputs():
    return ui.panel_main(
        ui.h2("Main Panel with Reactive Output"),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3('MLB Stats Dashboard through 2015'),
            ui.tags.br(),
            ui.output_text('baseball_record_count_string'),
            ui.tags.br(),
            ui.output_table('baseball_data_table'),
            ui.tags.br(),
            ui.h3('Filtered Summary Table'),
            output_widget('baseball_scatter_plot'),
            ui.tags.br(),
            output_widget('baseball_home_runs_scatter'),
            ui.tags.br(),
            output_widget('baseball_win_percentage_plot'),
            ui.tags.br(),
        ),
    )

