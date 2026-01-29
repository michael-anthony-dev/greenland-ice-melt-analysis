import pandas as pd
from datetime import datetime, timedelta

# --- CONFIGURATION ---
INPUT_FILE = 'greenland_mass_data.txt'
OUTPUT_FILE = 'greenland_cleaned.csv'

def decimal_year_to_date(decimal_year):
    """ Converts 2002.29 to a real date like 2002-04-16 """
    year = int(decimal_year)
    remainder = decimal_year - year
    base_date = datetime(year, 1, 1)
    days_in_year = 366 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 365
    return (base_date + timedelta(days=remainder * days_in_year)).date()

print("--- PROCESSING DATA ---")

try:
    # 1. Read the file (Skip the first 31 lines of text headers)
    # NOTE: If this fails, open your text file and count the header lines. 
    # You might need to change skiprows=31 to 35 or 40.
    df = pd.read_csv(INPUT_FILE, sep=r'\s+', header=None, skiprows=31)
    
    # 2. Select columns (Date, Mass, Uncertainty)
    df = df.iloc[:, 0:3] 
    df.columns = ['decimal_date', 'mass_change_gt', 'uncertainty']

    # 3. Convert Decimal Date to Regular Date
    df['record_date'] = df['decimal_date'].apply(decimal_year_to_date)

    # 4. Save to CSV
    final_df = df[['record_date', 'mass_change_gt', 'uncertainty']]
    final_df.to_csv(OUTPUT_FILE, index=False)

    print(f"✅ Success! Created: {OUTPUT_FILE}")
    print(final_df.head())

except Exception as e:
    print(f"❌ Error: {e}")
    print("Check if 'greenland_mass_data.txt' is in the folder and spelled correctly.")