from zipfile import ZipFile
import gradio as gr

# def greet(name):
#     return "Hello " + name + "!"

# demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
# def zip_to_json(file_obj):
#     files = []
#     with ZipFile(file_obj.name) as zfile:
#         for zinfo in zfile.infolist():
#             files.append(
#                 {
#                     "name": zinfo.filename,
#                     "file_size": zinfo.file_size,
#                     "compressed_size": zinfo.compress_size,
#                 }
#             )
#     return files

# files = gr.Interface(zip_to_json, "file", "json")
# gui = gr.Parallel(demo, files)

def update(name):
    return f"Welcome to Gradio, {name}!"

with gr.Blocks() as demo:
    gr.Markdown("Start typing below and then click **Run** to see the output.")
    with gr.Row():
        inp = gr.Textbox(placeholder="What is your name?")
        out = gr.Textbox()
    btn = gr.Button("Run")
    btn.click(fn=update, inputs=inp, outputs=out)

demo.launch()