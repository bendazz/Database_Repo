import sqlite3
import pandas as pd  
import gradio as gr  

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
WITH top_hitters AS (SELECT nameFirst,nameLast
FROM batting INNER JOIN people
ON batting.playerID = people.playerID
WHERE teamID = 'PHI'
GROUP BY batting.playerID
ORDER BY sum(HR) desc
LIMIT 10)

SELECT CONCAT(nameFirst,' ',nameLast) as player
FROM top_hitters
ORDER BY nameLast
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

players = []
for record in records:
    players.append(record[0])

print(players)