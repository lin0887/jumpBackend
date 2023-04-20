import pandas as pd
import re

# Load Excel file
excel_file = pd.ExcelFile('112跳繩各校名單.xlsx')

# Loop through all sheets and read data into DataFrame
all_df = pd.DataFrame(columns=['項目', '組別', '年級', '學校', '姓名', '指導老師', 'ID'])
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    #print(df.columns)
    tmp = df.columns
    df.columns = ['項目', '組別', '年級', '學校', '姓名', '指導老師', 'ID']
    df.loc[len(df), :] = tmp
    all_df = all_df.append(df)

all_df = all_df.sort_values(by=['ID'])

all_df.to_json('contestants.json', orient='records')
#all_df.to_excel('t.xlsx',index=False)
