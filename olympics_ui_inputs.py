"""
Purpose: Provide user interaction options for Summer dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""
from shiny import ui


def get_summer_inputs():
    return ui.panel_sidebar(
        ui.h2("Summer Olympics Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "Year_Range",
            "Year",
            min=1896,
            max=2012,
            value=[1896, 2012],
        ),
        ui.input_checkbox("SUMMER_MEDAL_GOLD", "Gold Medal", value=True),
        ui.input_checkbox("SUMMER_MEDAL_SILVER", "Silver Medal", value=True),
        ui.input_checkbox("SUMMER_MEDAL_BRONZE", "Bronze Medal", value=True),
        ui.input_radio_buttons(
            "ATHLETE_GENDER",
            "Select Genders",
            {"a": "All (includes missing values)", "f": "Female", "m": "Male"},
            selected="a",
        ),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Summer Olympics Table"),
            ui.tags.p("Description of each field in the table:"),
            ui.tags.ul(
                ui.tags.li("Year: Event Took Place"),
                ui.tags.li("City: City Where Event Took Place"),
                ui.tags.li("Sport: Sport of Event"),
                ui.tags.li("Discipline: Discipline of Event"),
                ui.tags.li("Athlete: Athlete Who Won Medal"),
                ui.tags.li("Country: Country of Athlete"),
                ui.tags.li("Gender: Male or Female"),
                ui.tags.li("Event: Event Name"),
                ui.tags.li("Medal: Type of Medal Won"),
            ),
            ui.output_table("summer_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
