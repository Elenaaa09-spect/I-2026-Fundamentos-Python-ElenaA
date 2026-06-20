import gradio

with gradio.Blocks() as demo:
    gradio.Markdown ("Registro")
    gradio.Textbox (label = "Nombre:")
    gradio.Button ("Enviar")

demo.launch()