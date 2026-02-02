import gradio as gr

def f(x,y):
    return x+y

with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            x = gr.Number(label = "type in x")
            y = gr.Number(label = "type in y")
            
        with gr.Column():
            sum = gr.Number(label = "this is the sum of these two numbers")

    x.change(fn = f, inputs = [x,y], outputs = [sum])
    y.change(fn = f, inputs = [x,y], outputs = [sum])

iface.launch()