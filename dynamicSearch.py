import gradio as gr   
import pandas as pd  
import sqlite3
from typing import Optional

def get_names(string):
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT nameFirst, nameLast, playerID
        FROM people
        WHERE nameLast LIKE ?
    """
    like = f"{string}%" if string is not None else "%"
    cursor.execute(query, [like])
    records = cursor.fetchall()
    conn.close()
    records_df = pd.DataFrame(records, columns=['First Name', 'Last Name', 'Player ID'])
    return records_df

def player_hr_df(player_id: Optional[str]) -> pd.DataFrame:
    if not player_id:
        return pd.DataFrame(columns=['Year', 'Home Runs'])
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT yearID, HR
        FROM batting
        WHERE playerID = ?
        ORDER BY yearID
    """
    cursor.execute(query, [player_id])
    records = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(records, columns=['Year', 'Home Runs'])
    return df

with gr.Blocks() as iface:
    text = gr.Textbox(label="Search", interactive=True)
    output = gr.DataFrame(headers=['First Name', 'Last Name', 'Player ID'], interactive=True)
    selected_id = gr.Textbox(label="Selected Player ID", interactive=False)
    plot = gr.LinePlot(x='Year', y='Home Runs', title='HR by Year')

    text.change(fn=get_names, inputs=text, outputs=output)

    def on_row_select(evt, df: pd.DataFrame):
        # evt.index is (row, col) for cell selections; use row index
        if evt is None or getattr(evt, 'index', None) is None:
            return None, pd.DataFrame(columns=['Year', 'Home Runs'])
        row = evt.index[0] if isinstance(evt.index, (tuple, list)) else evt.index
        try:
            pid = df.iloc[int(row)]['Player ID']
        except Exception:
            return None, pd.DataFrame(columns=['Year', 'Home Runs'])
        return str(pid), player_hr_df(pid)

    output.select(fn=on_row_select, inputs=output, outputs=[selected_id, plot])

iface.launch()
