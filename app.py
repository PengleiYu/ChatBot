from models import Conversation
import gradio as gr

conv = Conversation(10)


def answer(question, history):
    if history is None:
        history = []
    history.append(question)
    response = conv.ask(question)
    history.append(response)
    result = [(u, b) for u, b in zip(history[::2], history[1::2])]
    return result, history


with gr.Blocks(css="#chatbot{height:300px} .overflow-y-auto{height:500px}") as demo:
    chatbot = gr.Chatbot(elem_id='chatbot')
    state = gr.State([])

    with gr.Row():
        text = gr.Textbox(show_label=False, placeholder='Enter text and press enter').style(container=False)
    text.submit(answer, [text, state], [chatbot, state])

# 在本地启动时会卡住主线程，在notebook中则不会
demo.launch(server_name='0.0.0.0', server_port=8080, show_error=True)
