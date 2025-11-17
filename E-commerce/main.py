from fasthtml.common import *
from agent.ecommerce_agent import EcommerceAgent
from agent.state import ShoppingState
from ui.components import chat_bubble_user, chat_bubble_bot, left_side_card, product_card
import logfire
from dotenv import load_dotenv
import os

load_dotenv()
logfire.configure(token=os.getenv("LOGFIRE_TOKEN"))

app, rt = fast_app(
    pico=False,
    hdrs=(
        Script(src="https://unpkg.com/htmx.org@1.9.10"),
        Link(rel="stylesheet", href="/static/style.css")
    )
)


# Mount static files
from starlette.staticfiles import StaticFiles
app.mount('/static', StaticFiles(directory='static'), name='static')

agent = EcommerceAgent(api_key=os.getenv("GOOGLE_API_KEY"))
state = ShoppingState()


@rt("/")
def home():
    return Html(
        Head(
            Title("State Aware UI Agent"),
            Link(rel="stylesheet", href="/static/style.css"),
            Script(src="https://unpkg.com/htmx.org@1.9.10"),
            Script("""
                function scrollChatToBottom() {
                    const chatPanel = document.getElementById('chat-conversation');
                    if (chatPanel) {
                        chatPanel.scrollTop = chatPanel.scrollHeight;
                    }
                }
                document.addEventListener('htmx:afterSwap', scrollChatToBottom);
            """)
        ),
        Body(
            Div(
                H1("E-Commerce Assistant", cls="title"),
                Div(
                    # LEFT SIDE (Chat conversation)
                    Div(
                        H3("Chat", cls="section-title"),
                        Div(id="chat-conversation", cls="chat-panel"),
                        Form(
                            Input(
                                type="text",
                                name="message",
                                id="message-input",
                                placeholder="Type your message...",
                                required=True,
                                cls="chat-input",
                                autofocus=True
                            ),
                            Button("Send", type="submit", cls="send-btn"),
                            hx_post="/chat",
                            hx_target="#chat-conversation",
                            hx_swap="beforeend",
                            hx_on__after_request="this.reset(); document.getElementById('message-input').focus()",
                            cls="chat-form"
                        ),
                        cls="left-container"
                    ),

                    # RIGHT SIDE (Product cards)
                    Div(
                        H3("Shopping Cart", cls="section-title"),
                        Div(id="cart-items", cls="cart-panel"),
                        cls="right-container"
                    ),
                    cls="main-wrapper"
                )
            )
        )
    )


@rt("/chat")
def chat(message: str):
    logfire.info("User message received", message=message)
    
    # Add user message bubble
    user_ui = chat_bubble_user(message)

    # Process
    with logfire.span("Agent processing"):
        result = agent.process_message(message, state.get_state_info())
        bot_msg = result["message"]
        logfire.info("Agent response", response=bot_msg, actions=result["actions"])

    # Add bot response bubble
    bot_ui = chat_bubble_bot(bot_msg)

    # Perform actions
    for action in result["actions"]:
        t = action["type"]
        logfire.info("Executing action", action_type=t, action=action)

        if t == "add_item":
            product = action.get("product")
            qty = action.get("quantity", 1)
            color = action.get("color", "")
            state.add_to_cart(product, qty, color)
        elif t == "remove_item":
            product_name = action.get("product_name")
            state.remove_from_cart(product_name)
        elif t == "reduce_quantity":
            product_name = action.get("product_name")
            qty = action.get("quantity", 1)
            state.reduce_quantity(product_name, qty)
        elif t == "update_quantity":
            product_name = action.get("product_name")
            qty = action.get("quantity", 1)
            state.update_quantity(product_name, qty)
        elif t == "clear_cart":
            state.clear_cart()
        elif t == "save_name":
            name = action.get("name", "")
            if name:
                state.set_user_name(name)
                logfire.info("User name saved", name=name)

    # Build product cards for cart items
    cards = []
    for product, qty in state.get_cart_items():
        cards.append(product_card(product.name, qty, product.color))
    
    logfire.info("Cart updated", cart_items=len(cards), state=state.get_state_info())

    # Return chat messages to left panel and product cards to right panel
    return (
        user_ui,
        bot_ui,
        Div(
            *cards,
            hx_swap_oob="innerHTML:#cart-items",
            id="temp-cart"
        )
    )


serve()
