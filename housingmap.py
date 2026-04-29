"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""

import pandas as pd
import plotly.express as px


def main():
    input_csv = input("Enter input file: ")
    choice = input("Enter number of bedrooms (0 for studio, 1 for one bedroom,...): ")
    output_html = input("Enter output file name: ")

    column_mapping = {
        "0": "Studio Units",
        "1": "1-BR Units",
        "2": "2-BR Units",
        "3": "3-BR Units",
        "4": "4-BR Units",
        "5": "5-BR Units",
    }
    unit_col = column_mapping.get(choice, "6-BR+ Units")

    housing_df = pd.read_csv(input_csv)
    housing_df = housing_df[housing_df["Project Name"] != "Confidential"]
    df = housing_df[housing_df[unit_col].notnull()].copy()

    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        size=unit_col,
        hover_name="Project Name",
        hover_data={"Latitude": True, "Longitude": True, unit_col: True},
        title=f"Housing: {unit_col}",
        zoom=10,
        mapbox_style="carto-positron",
    )

    fig.write_html(output_html)


if __name__ == "__main__":
    main()
