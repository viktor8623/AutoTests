import pandas as pd

from model.tickets import Tickets


df = pd.read_excel("../data/tickets.xlsx", "Successful", dtype=str, keep_default_na=False)

excel_dict = df.to_dict(orient='records')

testdata = []

for item in excel_dict:
    for key in item:
        if item[key] == "":
            item[key] = None
    testdata.append(Tickets(**item))
