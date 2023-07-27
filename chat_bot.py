from models import Conversation
import gradio as gr

prompt = """你是一个中国厨师，用中文回答做菜的问题。你的回答需要满足以下要求:1. 你的回答必须是中文2. 回答限制在100个字以内"""
conv = Conversation(prompt, 10)


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
