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
        ui.tags.section(
            ui.h3("Team Data Table"),
            ui.tags.p("Description of each field in the table:"),
            ui.tags.ul(
                ui.tags.li("yearID: The year"),
                ui.tags.li("lgID: League ID"),
                ui.tags.li("teamID: Team ID"),
                ui.tags.li("franchID: Franchise ID"),
                ui.tags.li("divID: Division ID"),
                ui.tags.li("Rank: Team's rank"),
                ui.tags.li("G: Number of games played"),
                ui.tags.li("Ghome: Number of home games played"),
                ui.tags.li("W: Number of games won"),
                ui.tags.li("L: Number of games lost"),
                ui.tags.li("DivWin: Division win indicator"),
                ui.tags.li("WCWin: Wild Card win indicator"),
                ui.tags.li("LgWin: League win indicator"),
                ui.tags.li("WSWin: World Series win indicator"),
                ui.tags.li("R: Number of runs scored"),
                ui.tags.li("AB: Number of at-bats"),
                ui.tags.li("H: Number of hits"),
                ui.tags.li("2B: Number of doubles"),
                ui.tags.li("3B: Number of triples"),
                ui.tags.li("HR: Number of home runs"),
                ui.tags.li("BB: Number of walks"),
                ui.tags.li("SO: Number of strikeouts"),
                ui.tags.li("SB: Number of stolen bases"),
                ui.tags.li("CS: Number of times caught stealing"),
                ui.tags.li("HBP: Number of times hit by pitch"),
                ui.tags.li("SF: Number of sacrifice flies"),
                ui.tags.li("RA: Number of runs allowed"),
                ui.tags.li("ER: Number of earned runs"),
                ui.tags.li("ERA: Earned run average"),
                ui.tags.li("CG: Number of complete games"),
                ui.tags.li("SHO: Number of shutouts"),
                ui.tags.li("SV: Number of saves"),
                ui.tags.li("IPouts: Number of outs pitched"),
                ui.tags.li("HA: Number of hits allowed"),
                ui.tags.li("HRA: Number of home runs allowed"),
                ui.tags.li("BBA: Number of walks allowed"),
                ui.tags.li("SOA: Number of strikeouts by pitchers"),
                ui.tags.li("E: Number of errors"),
                ui.tags.li("DP: Number of double plays"),
                ui.tags.li("FP: Fielding percentage"),
                ui.tags.li("name: Team name"),
                ui.tags.li("park: Team's home park"),
                ui.tags.li("attendance: Attendance"),
                ui.tags.li("BPF: Batting park factor"),
                ui.tags.li("PPF: Pitching park factor"),
                ui.tags.li("teamIDBR: Team ID (Baseball-Reference)"),
                ui.tags.li("teamIDlahman45: Team ID (Lahman Database version 4.5)"),
                ui.tags.li("teamIDretro: Team ID (Retrosheet)"),
            ),
            ui.output_table("team_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )