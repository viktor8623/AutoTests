import pandas as pd

from model.tickets import Tickets


df1 = pd.read_excel("../data/tickets.xlsx", "Successful", dtype=str, keep_default_na=False)
df2 = pd.read_excel("../data/tickets.xlsx", "Declined", dtype=str, keep_default_na=False)

excel_dict1 = df1.to_dict(orient='records')
excel_dict2 = df2.to_dict(orient='records')

testdata1 = []
testdata2 = []


def extract_test_data(testdata, excel_dict):
    for item in excel_dict:
        for key in item:
            if item[key] == "":
                item[key] = None
        testdata.append(Tickets(**item))


extract_test_data(testdata1, excel_dict1)
extract_test_data(testdata2, excel_dict2)
