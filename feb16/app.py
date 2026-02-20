import sqlite3
import pandas as pd  
import gradio as gr  

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
WITH top_hitters AS (SELECT nameFirst,nameLast,batting.playerID  
FROM batting INNER JOIN people
ON batting.playerID = people.playerID
WHERE teamID = 'PHI'
GROUP BY batting.playerID
ORDER BY sum(HR) desc
LIMIT 10)

SELECT CONCAT(nameFirst,' ',nameLast) as player,playerID
FROM top_hitters
ORDER BY nameLast
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

def f(playerID):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
    SELECT CAST(yearID AS text),HR
    FROM Batting
    WHERE teamID = 'PHI' AND playerID = ?
    """
    cursor.execute(query,[playerID])
    records = cursor.fetchall()
    conn.close() 
    df = pd.DataFrame(records,columns = ["year","home runs"]) 
    return df



with gr.Blocks() as iface:
    player_dd = gr.Dropdown(records,interactive = True)
    plot = gr.LinePlot(x = "year", y = "home runs" )
    player_dd.change(fn = f,inputs = [player_dd],outputs = [plot])

iface.launch()