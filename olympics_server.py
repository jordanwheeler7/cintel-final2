""" 
Purpose: Provide reactive output for the summer dataset.

- Use inputs from the UI Sidebar to filter the dataset.
- Update reactive outputs in the UI Main Panel.

Matching the IDs in the UI Sidebar and function/output names in the UI Main Panel
to this server code is critical. They are case sensitive and must match exactly.

"""
import pathlib
from shiny import render, reactive
import matplotlib.pyplot as plt
import pandas as pd
from plotnine import aes, geom_point, ggplot, ggtitle
from shinywidgets import render_widget
import plotly.express as px

from util_logger import setup_logger

logger, logname = setup_logger(__name__)


def get_summer_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    p = pathlib.Path(__file__).parent.joinpath("data").joinpath("summer.csv")
    # logger.info(f"Reading data from {p}")
    original_df = pd.read_csv(p)
    total_count = len(original_df)

    reactive_df = reactive.Value()

    @reactive.Effect
    @reactive.event(
        input.SUMMER_YEAR_RANGE,
        input.SUMMER_MEDAL_GOLD,
        input.SUMMER_MEDAL_SILVER,
        input.SUMMER_MEDAL_BRONZE,
        input.ATHLETE_GENDER,
    )
    def _():
        df = original_df.copy()

        input_range = input.SUMMER_YEAR_RANGE() # this is a tuple 
        input_min = input_range[0]
        input_max = input_range[1]
        
        year_filter = (df["year"] >= input_min) & (df["year"] <= input_max)
        df = df[year_filter]    

        """
        Filter the dataframe to bassed on selection of medals and year range
        
        """
        
        display_medal = []
        if input.SUMMER_MEDAL_GOLD():
            display_medal.append("Gold")
        if input.SUMMER_MEDAL_SILVER():
            display_medal.append("Silver")
        if input.SUMMER_MEDAL_BRONZE():
            display_medal.append("Bronze")
        display_medal = display_medal or ["Gold", "Silver", "Bronze"]
        medals_filter = df["medal"].isin(display_medal)
        df = df[medals_filter]
        
        input_gender = input.ATHLETE_GENDER()
        gender_dict = {"a": ["M", "F"], "f": ["F"], "m": ["M"]}
        if input_gender != "a":
            gender_filter = df["gender"] == gender_dict[input_gender]
            df = df[gender_filter]

        # Set the reactive value
        reactive_df.set(df)

    @output
    @render.text
    def summer_record_count_string():
        filtered_df = reactive_df.get()
        filtered_count = len(filtered_df)
        message = f"Showing {filtered_count} of {total_count} records"
        # logger.debug(f"filter message: {message}")
        return message

    @output
    @render.table
    def summer_filtered_table():
        filtered_df = reactive_df.get()
        return filtered_df

    @output
    @render_widget
    def summer_output_widget1():
        df = reactive_df.get()
        plotly_express_plot = px.scatter(df, x="discipline", y="medal", color="event", size="year")
        plotly_express_plot.update_layout(title="Summer Olympics with Plotly Express")
        return plotly_express_plot

    @output
    @render.plot
    def summer_plot1():
        df = reactive_df.get()
        matplotlib_fig, ax = plt.subplots()
        plt.title("Summer with matplotlib")
        ax.scatter(df["medal"], df["country"])
        return matplotlib_fig

    @output
    @render_widget
    def summer_plot3():
        df = reactive_df.get()
        plotly_express_plot2 = px.scatter(df, x="discipline", y="medal", symbol ="country", size="year")
        plotly_express_plot2.update_layout(title="Summer Olympics with Plotly Express")
        
        return plotly_express_plot2
        

    # return a list of function names for use in reactive outputs
    return [
        summer_record_count_string,
        summer_filtered_table,
        summer_output_widget1,
        summer_plot1,
        summer_plot3
    ]
