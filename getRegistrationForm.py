import pandas as pd
import numpy as np
import re

# Load Excel file
excel_file = pd.ExcelFile('..\\名單\\112跳繩各校名單.xlsx')

col = ['項目', '組別', '年級', '學校', '姓名', '指導老師', 'ID']
# Loop through all sheets and read data into DataFrame
all_df = pd.DataFrame(columns = col)
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    tmp = df.columns
    df.columns = col
    df.loc[len(df), :] = tmp
    
    all_df = all_df.append(df)

all_df['成績'] = np.zeros(len(all_df), dtype=int)
all_df['等第'] = np.full(len(all_df),np.nan)
  
all_df = all_df.sort_values(by=['ID'])

all_df.to_json('contestants.json', orient='records')

