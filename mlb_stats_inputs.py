"""
Purpose: Provide user interaction options for MT Cars dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""
from shiny import ui
import randfacts
# Define the UI inputs and include our new selection options

def get_baseball_data_inputs():
    return ui.panel_sidebar(
        ui.h2("Here is a random fact for you to enjoy!"),
        ui.h5(randfacts.getFact()),
        ui.hr(),
        ui.h2("MLB Teams Interaction"),
        ui.tags.hr(),
        ui.input_select(
            id="SELECTED_TEAM",
            label="Choose a team",
            choices=["All Teams", "Arizona Diamondbacks", "Atlanta Braves", "Baltimore Orioles", "Boston Red Sox", "Chicago Cubs", "Chicago White Sox", "Cincinnati Reds", "Cleveland Indians", "Colorado Rockies", "Detroit Tigers", "Houston Astros", "Kansas City Royals", "Los Angeles Angels", "Los Angeles Dodgers", "Miami Marlins", "Milwaukee Brewers", "Minnesota Twins", "New York Mets", "New York Yankees", "Oakland Athletics", "Philadelphia Phillies", "Pittsburgh Pirates", "San Diego Padres", "San Francisco Giants", "Seattle Mariners", "St. Louis Cardinals", "Tampa Bay Rays", "Texas Rangers", "Toronto Blue Jays", "Washington Nationals"],
            selected="Kansas City Royals",
        ),
        ui.tags.hr(),
        ui.input_slider(
            id="SELECTED_YEAR",
            label="Select a year range",
            min=1876,
            max=2015,
            value=[1876, 2015],
            step=1,
        ),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Team Data Table"),
            ui.tags.p("Description of each field in the table:"),
            ui.tags.ul(
                ui.tags.li("yearID: The year"),
                ui.tags.li("G: Number of games played"),
                ui.tags.li("W: Number of games won"),
                ui.tags.li("L: Number of games lost"),
                ui.tags.li("DivWin: Division win indicator"),
                ui.tags.li("WSWin: World Series win indicator"),
                ui.tags.li("R: Number of runs scored"),
                ui.tags.li("H: Number of hits"),
                ui.tags.li("RA: Number of runs allowed"),
                ui.tags.li("ER: Number of earned runs"),
                ui.tags.li("ERA: Earned run average"),
            ),
            ui.output_table("team_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )