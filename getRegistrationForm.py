import pandas as pd
import re

# 讀取Excel檔案
excel_file = pd.ExcelFile("112v.xlsx")


# read all sheets
all_df = pd.DataFrame()
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    sheet_df = pd.read_excel("112v.xlsx", sheet_name=sheet_name, header=None)
    all_df = all_df.append(sheet_df, ignore_index=True)

# 加上欄位名稱
all_df.columns = ["項目", "組別", "年級", "學校", "選手", "教練", "編號"]
all_df.rename (columns={"項目": "contest", "組別": "group", "年級": "grade", "學校": "school", "選手": "name", "教練": "teacher", "編號": "id"},inplace=True)
all_df.dropna(subset=["id"], inplace=True)
all_df.to_json("contestants.json", orient="records")

