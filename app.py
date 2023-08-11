"""
Purpose: Use Python to create a continuous intelligence and 
interactive analytics dashboard using Shiny for Python with 
interactive charts from HoloViews Bokeh and Plotly Express.

Each Shiny app has two parts: 

- a user interface app_ui object (similar to the HTML in a web page) 
- a server function that provides the logic for the app (similar to JS in a web page).

"""
from shiny import App, ui
import shinyswatch

from mtcars_server import get_mtcars_server_functions
from mtcars_ui_inputs import get_mtcars_inputs
from mtcars_ui_outputs import get_mtcars_outputs

from penguins_server import get_penguins_server_functions
from penguins_ui_inputs import get_penguins_inputs
from penguins_ui_outputs import get_penguins_outputs

from relationships_server import get_relationships_server_functions
from relationships_ui_inputs import get_relationships_inputs
from relationships_ui_outputs import get_relationships_outputs

from olympics_server import get_summer_server_functions
from olympics_ui_inputs import get_summer_inputs
from olympics_ui_outputs import get_summer_outputs

from mlb_stats_inputs import get_baseball_data_inputs
from mlb_stats_outputs import get_baseball_data_outputs
from mlb_stats_server import get_baseball_data_server_functions

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

app_ui = ui.page_navbar(
    shinyswatch.theme.solar(),
    ui.nav(
        "MLB Stats",
        ui.layout_sidebar(
            get_baseball_data_inputs(),
            get_baseball_data_outputs(),
        ),
    ),
    ui.nav(
        "MT_Cars",
        ui.layout_sidebar(
            get_mtcars_inputs(),
            get_mtcars_outputs(),
        ),
    ),
    ui.nav(
        "Penguins",
        ui.layout_sidebar(
            get_penguins_inputs(),
            get_penguins_outputs(),
        ),
    ),
    ui.nav(
        "Relationships",
        ui.layout_sidebar(
            get_relationships_inputs(),
            get_relationships_outputs(),
        ),
    ),
    ui.nav(
        "Olympics",
        ui.layout_sidebar(
            get_summer_inputs(),
            get_summer_outputs(),
        ),
    ),
    ui.nav(ui.a("About", href="https://github.com/jordanwheeler7")),
    ui.nav(ui.a("GitHub", href="https://github.com/jordanwheeler7/cintel-final")),
    ui.nav(ui.a("App", href="https://jordan-wheeler7.shinyapps.io/cintel-final/")),
    ui.nav(ui.a("Examples", href="https://shinylive.io/py/examples/")),
    ui.nav(ui.a("Widgets", href="https://shiny.rstudio.com/py/docs/ipywidgets.html")),
    ui.nav(ui.a("MLB Stats", href="https://www.baseball-reference.com/teams/")),
    title=ui.h1("Wheeler Dashboard"),
)

def server(input, output, session):
    """Define functions to create UI outputs."""
    logger.info("Starting server...")
    
    # Initialize the reactive outputs for each Shiny application
    team_data_server_functions = get_baseball_data_server_functions(input, output, session)
    mtcars_server_functions = get_mtcars_server_functions(input, output, session)
    penguins_server_functions = get_penguins_server_functions(input, output, session)
    relationships_server_functions = get_relationships_server_functions(input, output, session)
    summer_server_functions = get_summer_server_functions(input, output, session)

    # Merge all reactive outputs into a single list
    all_reactive_outputs = (
        team_data_server_functions
        + mtcars_server_functions
        + penguins_server_functions
        + relationships_server_functions
        + summer_server_functions
    )
    
    return all_reactive_outputs

app = App(app_ui, server)