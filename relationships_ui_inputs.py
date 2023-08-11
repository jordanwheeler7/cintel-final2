"""
Purpose: Provide user interaction options for the relationships dataset.

"""
from shiny import ui
from htmltools import head_content, HTML

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

bokeh_dependency = None
try:
    from bokeh.resources import Resources

    bokeh_dependency = head_content(HTML(Resources(mode="inline").render()))
except ImportError:
    logger.warn("Could not import bokeh")


def get_relationships_inputs():
    return bokeh_dependency, ui.panel_sidebar(
        ui.h2("Relationships Interaction"),
        ui.input_switch("RELATIONSHIPS_SHOW_TOGGLE", "Show Charts", value=True),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
