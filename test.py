import pandas as pd
import re

# Load Excel file
excel_file = pd.ExcelFile('111v.xlsx')

# Loop through all sheets and read data into DataFrame
all_df = pd.DataFrame()
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    if re.match(r"[A-Za-z]\d+$", sheet_name):
        df.rename(columns={'指導\n老師': '指導老師'}, inplace=True)
        all_df = all_df.append(df.loc[:, ['項目', '組別', '年級', '學校', '姓名', '指導老師', '號碼', '成績']], ignore_index=True)

all_df.rename(columns={'項目': 'contest', '組別': 'group', '年級': 'grade', '學校': 'school', '姓名': 'name', '指導老師': 'teacher', '號碼': 'id', '成績': 'score'}, inplace=True)
all_df.dropna(subset=['id'], inplace=True)
all_df.to_json('contestants.json', orient='records')
