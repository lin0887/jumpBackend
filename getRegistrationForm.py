import pandas as pd
import re
import numpy as np

# Load Excel file


# 讀取Excel檔案
excel_file = pd.ExcelFile("..\\名單\\112跳繩各校名單.xlsx")


# read all sheets
all_df = pd.DataFrame()
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    sheet_df = pd.read_excel("..\\名單\\112跳繩各校名單.xlsx", sheet_name=sheet_name, header=None)
    sheet_df.columns = ["contest", "group", "grade", "school", "name", "teacher", "id"]
    sheet_df.dropna(subset=["id"], inplace=True)
    sheet_df["id"] = sheet_df["id"].astype(int)
    all_df = all_df.append(sheet_df, ignore_index=True)

# 加上欄位名稱
# all_df.columns = ["contest", "group", "grade", "school", "name", "teacher", "id"]
# id to string
all_df['score'] =  np.zeros(len(all_df), dtype=int)
all_df["id"] = all_df["id"].astype(str)
all_df.to_json("contestants.json", orient="records")

    

# all_df.rename(columns={'項目': 'contest', '組別': 'group', '年級': 'grade', '學校': 'school', '姓名': 'name', '指導老師': 'teacher', '號碼': 'id', '成績': 'score'}, inplace=True)
# all_df.dropna(subset=['id'], inplace=True)
# all_df.to_json('contestants.json', orient='records')
