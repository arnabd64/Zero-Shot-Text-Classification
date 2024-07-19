import gradio as gr
import gradio.components as gc

from webapp.inference import classify

with gr.Blocks() as app:
    
    with open("webapp/assets/introduction.md") as md:
        intro = md.read()
    
    gr.Markdown(intro)
    
    with gr.Tab(label="Inference"):
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    text_input = gc.Textbox(lines=3, max_lines=20, label="Input Text")
                
                with gr.Row():
                    labels = gc.Textbox(lines=1, label="Candidate Labels", info="Comma separated Labels")
                    
                with gr.Row():
                    submit = gc.Button("Submit")
                
            with gr.Column():
                label_output = gc.Label(label="Label Scores")
                
        submit.click(classify, inputs=[text_input, labels], outputs=[label_output], queue=True)
        
    with gr.Tab(label="Help"):
        with open("webapp/assets/help.md") as md:
            help = md.read()
        gr.Markdown(help)
        
    with gr.Tab(label="About"):
        with open("webapp/assets/about.md") as md:
            about = md.read()
        gr.Markdown(about)