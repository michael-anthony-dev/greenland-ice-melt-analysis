import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# --- CONNECT TO DB ---
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password', 
    database='climate_db'
)

# --- QUERY DATA ---
query = "SELECT record_date, mass_change FROM greenland_mass ORDER BY record_date"
df = pd.read_sql(query, conn)

# --- PLOT ---
plt.figure(figsize=(10, 6))

# Plot the data
plt.plot(df['record_date'], df['mass_change'], label='Mass Change (Gt)', color='red')

# Add trend line (Moving Average)
df['ma'] = df['mass_change'].rolling(window=12).mean()
plt.plot(df['record_date'], df['ma'], label='12-Month Average', color='blue', linewidth=2)

# Styling
plt.title('Greenland Ice Sheet Mass Loss (2002-Present)')
plt.xlabel('Year')
plt.ylabel('Mass Change (Gigatonnes)')
plt.axhline(0, color='black', linewidth=0.8) # Zero line
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# Save it
plt.savefig('final_graph.png')
print("Graph saved as final_graph.png")