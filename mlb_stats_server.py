import pandas as pd
from shiny import render, reactive
from shinywidgets import render_widget
import plotly.express as px
import pathlib
from util_logger import setup_logger
from datetime import datetime
from plotnine import ggplot, aes, geom_point, ggtitle
import matplotlib.pyplot as plt
import plotly


logger, logname = setup_logger(__name__)

# Load data from the CSV file
p = pathlib.Path(__file__).parent.joinpath("data").joinpath("baseball.csv")
original_df = pd.read_csv(p)
total_count = len(original_df)

# Define your reactive functions based on user inputs
def get_baseball_data_server_functions(input, output, session):
    reactive_df = reactive.Value()

    @reactive.Effect
    @reactive.event(input.SELECTED_TEAM)
    def _():
        selected_team = input.SELECTED_TEAM()
        df = original_df[original_df["name"] == selected_team].copy()

        # Update the reactive DataFrame
        reactive_df.set(df)

    @output
    @render.text
    def baseball_record_count_string():
        filtered_df = reactive_df.get()
        filtered_count = len(filtered_df)
        message = f"Showing {filtered_count} records for selected team"
        return message

    @output
    @render.table
    def baseball_data_table():
        filtered_df = reactive_df.get()
        return filtered_df[["yearID", "G", "W", "L"]]

    @output
    @render_widget
    def baseball_scatter_plot():
        df = reactive_df.get()
        plot = px.scatter(df, x="yearID", y="HR", color="HR", title="Home Runs Over Years")
        return plot

    @output
    @render_widget
    def baseball_home_runs_scatter():
        df = reactive_df.get()
        plot = px.scatter(df, x="yearID", y="HR", color="HR", title="Home Runs Over Years")
        return plot


    @output
    @render_widget
    def baseball_win_percentage_plot():
        df = reactive_df.get()
        df["Win_Percentage"] = df["W"] / (df["W"] + df["L"]) * 100
        plot = px.line(df, x="yearID", y="Win_Percentage", title="Win Percentage Over Years")
        return plot

    return [
        baseball_record_count_string,
        baseball_data_table,
        baseball_scatter_plot,
        baseball_home_runs_scatter,
        baseball_win_percentage_plot
    ]
