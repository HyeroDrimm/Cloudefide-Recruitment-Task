import pandas as pd
from solution import add_virtual_column

df = pd.read_csv('sales.csv')

df = df.rename(columns={"Quantity ": "Quantity", "Unit Price": "Unit_Price", "Order Date": "Order_Date", "Order ID":"Order_ID"}, errors="raise")

df = df[~df["Order_ID"].isin(["Order ID", "TOTAL"])]

cleaned_quantity = df["Quantity"].str.replace(" ", "", regex=False)
df["Quantity"] = pd.to_numeric(cleaned_quantity, errors="coerce")

cleaned_unit_price = df["Unit_Price"].str.replace(" ", "", regex=False).str.replace(",", ".", regex=False)
df["Unit_Price"] = pd.to_numeric(cleaned_unit_price, errors="coerce")

# Replace missing unit prices
df.loc[(df["Product"] == "Keyboard") & df["Unit_Price"].isna(), "Unit_Price"] = 89.
df.loc[(df["Product"] == "Printer paper") & df["Unit_Price"].isna(), "Unit_Price"] = 21.

df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce").fillna(0)

df["Region"] = df["Region"].str.strip().str.capitalize()

df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%Y-%m-%d", errors="coerce")

df = add_virtual_column(df, "(Quantity * Unit_Price - Discount).round(2)", "revenue")

revenue_by_region_df = df.groupby("Region")["revenue"].sum()
revenue_by_region_df.to_csv(" revenue_by_region.csv", index=True)
