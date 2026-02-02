import gradio as gr   
import pandas as pd  
import sqlite3


conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()
query = """
    WITH topHitters AS(
        SELECT nameFirst,nameLast,batting.playerID as playerID
        FROM batting inner join people
        ON batting.playerID = people.playerID
        WHERE teamID = 'PHI'
        GROUP BY batting.playerID
        ORDER BY sum(HR) desc
        LIMIT 10)
    SELECT NameFirst,NameLast,playerID
    FROM topHitters
    ORDER BY NameLast 


"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()


players = []
for record in records:
    first = record[0]
    last = record[1]
    name = f"{record[0]} {record[1]}"
    players.append((name,record[2]))

def f(id):
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT CAST(yearID AS TEXT) AS Year,HR
               
        FROM batting
        WHERE playerID = ?
        ORDER BY yearID
    """
    cursor.execute(query,[id])
    records = cursor.fetchall()
    conn.close()
    records_df = pd.DataFrame(records, columns=['Year', 'Home Runs'])
    return records_df

    




with gr.Blocks() as iface:
    dd = gr.Dropdown(choices=players, label="Select player", interactive=True)
    plot = gr.LinePlot(x='Year', y='Home Runs')
    dd.change(fn=f, inputs=dd, outputs=plot)

iface.launch()




