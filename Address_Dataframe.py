"""
Jasmine Carrion
jasmine.carrion73@login.cuny.edu
"""
import pandas as pd


def make_addr_df(last_names, first_names, emails):
    data = {
        "Last": last_names.split(),
        "First": first_names.split(),
        "emails": emails.split(),
    }
    return pd.DataFrame(data)
