import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
   SELECT teamID, sum(HR) as seasonHR
    FROM batting
    WHERE yearID = 2025
    GROUP BY teamID
    HAVING seasonHR >= 200
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records,columns = ['team','homeruns'])

print(records_df)