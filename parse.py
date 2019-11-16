import json
import pandas as pd
import openpyxl
from pandas.io.json import json_normalize

with open('imdb.json') as imdb_json:
    json_data=json.load(imdb_json)
json_file = pd.DataFrame.from_dict(json_normalize(json_data))
json_file.sort_values("rating",ascending=False,inplace=True)
json_file.to_excel('final_output.xlsx')

