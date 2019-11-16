import json
import pandas as pd
from pandas.io.json import json_normalize

with open('imdb.json') as imdb_json:
    json_data=json.load(imdb_json)
json_file = pd.DataFrame.from_dict(json_normalize(json_data))
print(json_file)
