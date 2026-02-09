import sqlite3
import pandas as pd  

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT teamID, sum(HR)
    FROM batting
    WHERE yearID = 2025
    GROUP BY teamID 
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records,columns = ['yearID','totalHR'])

print(records_df)