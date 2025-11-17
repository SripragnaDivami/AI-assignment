from fasthtml import Div

def chat_bubble_user(message: str):
    return Div(
        Div(message, cls="bubble user-bubble"),
        cls="bubble-row user-row"
    )

def chat_bubble_bot(message: str):
    return Div(
        Div(message, cls="bubble bot-bubble"),
        cls="bubble-row bot-row"
    )

def left_side_card(title: str, content: str):
    return Div(
        Div(title, cls="card-title"),
        Div(content, cls="card-body"),
        cls="left-card"
    )
