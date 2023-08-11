""" 
Purpose: Provide reactive output for the relationships dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

See: https://holoviews.org/reference/elements/bokeh/Chord.html

"""
import pandas as pd
import holoviews as hv
from holoviews import opts, dim
from bokeh.sampledata.les_mis import data
import jupyter_bokeh as jbk
from shinywidgets import render_widget
from util_logger import setup_logger

logger, logname = setup_logger(__name__)
hv.extension("bokeh")


def get_relationships_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    # get a pandas dataframe of the links and the nodes
    df_links = pd.DataFrame(data["links"])
    df_nodes = pd.DataFrame(data["nodes"])

    # get a holoviews dataset of nodes. the 'index' column is the node id
    nodes = hv.Dataset(df_nodes, "index")

    @output
    @render_widget
    def relationships_output_widget1():
        if input.RELATIONSHIPS_SHOW_TOGGLE():
            # logger.info("UI inputs changed. Updating relationships output widget2")

            # create a chord diagram from the links and the nodes
            # value = (5, None) only links with a value 5+ will be shown
            chord = hv.Chord((df_links, nodes)).select(value=(5, None))

            # Set some chart options
            # Category20 is a color palette
            # The edge_color is based on the source node
            # The node_color is based on the index (node id)
            # The labels are the names of the nodes (from the name column)
            chord.opts(
                opts.Chord(
                    cmap="Category20",
                    edge_cmap="Category20",
                    edge_color=dim("source").str(),
                    labels="name",
                    node_color=dim("index").str(),
                    title="Les Misérables Relationships 5+ (HoloViews Bokeh)",
                    width=800,
                    height=800,
                )
            )

            widget = hv.render(chord, backend="bokeh")
            wrapped_widget = jbk.BokehModel(widget)
            return wrapped_widget
        else:
            return None

    # return a list of function names for use in reactive outputs
    return [
        relationships_output_widget1,
    ]
