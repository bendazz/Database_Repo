import sqlite3
import gradio as gr  

def fetch_phillies():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT playerID
        FROM batting
        WHERE teamID = 'PHI' AND yearID = 1976
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    players = []
    for record in records:
        players.append(record[0])
    return players
    
def f(player):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT HR
        FROM batting
        WHERE playerID = ? AND yearID = 1976 AND teamID = 'PHI'
    """
    cursor.execute(query,[player]) 
    records = cursor.fetchall()
    return records[0][0]

with gr.Blocks() as iface:
    playerID = gr.Dropdown(choices = fetch_phillies(),interactive = True)
    homeruns = gr.Number()
    playerID.change(fn = f,  inputs=[playerID],  outputs=[homeruns])

iface.launch()



