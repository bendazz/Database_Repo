import sqlite3
import gradio as gr  
import pandas as pd  

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()
query = """
WITH top_hitters AS(
    SELECT nameFirst, nameLast, batting.playerID as id
    FROM batting INNER JOIN people
    ON batting.playerID = people.playerID
    WHERE teamID = 'PHI'
    GROUP BY batting.playerID
    ORDER BY sum(HR) desc
    LIMIT 10
    ) 

SELECT CONCAT(nameFirst,' ',nameLast),id
FROM top_hitters
ORDER BY nameLast
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

players = []
for record in records:
    players.append(record[0])

def f(id):
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT CAST(yearID AS TEXT),HR
        FROM batting
        WHERE teamID = 'PHI' AND playerID = ?
        ORDER BY yearID
    """
    cursor.execute(query, [id])
    records = cursor.fetchall()
    conn.close()
    records_df = pd.DataFrame(records, columns = ['Year','Home Runs'])
    return records_df


with gr.Blocks() as iface:
      name_box = gr.Dropdown(choices = records,interactive = True)
      plot = gr.LinePlot(x = 'Year',y = 'Home Runs',y_lim = [0,60])
      name_box.change(fn = f, inputs = [name_box], outputs = plot)

iface.launch()