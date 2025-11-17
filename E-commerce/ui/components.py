from fasthtml.common import *

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

def product_card(name: str, quantity: int, color: str = ""):
    # Color mapping for specific colors
    color_gradients = {
        "pink": "linear-gradient(135deg, #ff6b9d 0%, #f06595 100%)",
        "red": "linear-gradient(135deg, #ff6b6b 0%, #c92a2a 100%)",
        "blue": "linear-gradient(135deg, #4dabf7 0%, #228be6 100%)",
        "green": "linear-gradient(135deg, #51cf66 0%, #37b24d 100%)",
        "yellow": "linear-gradient(135deg, #ffd43b 0%, #fab005 100%)",
        "orange": "linear-gradient(135deg, #ff922b 0%, #fd7e14 100%)",
        "purple": "linear-gradient(135deg, #9775fa 0%, #7950f2 100%)",
        "black": "linear-gradient(135deg, #343a40 0%, #1a1e21 100%)",
        "white": "linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)",
        "gray": "linear-gradient(135deg, #868e96 0%, #495057 100%)",
    }
    
    # If color is specified, use it
    if color and color.lower() in color_gradients:
        gradient = color_gradients[color.lower()]
    else:
        # Color mapping for different products (fallback)
        color_map = {
        # Fruits
        "apple": "linear-gradient(135deg, #ff6b6b 0%, #c92a2a 100%)",  # Red
        "apples": "linear-gradient(135deg, #ff6b6b 0%, #c92a2a 100%)",
        "mango": "linear-gradient(135deg, #ffd43b 0%, #fab005 100%)",  # Yellow/Gold
        "mangoes": "linear-gradient(135deg, #ffd43b 0%, #fab005 100%)",
        "banana": "linear-gradient(135deg, #ffe066 0%, #fcc419 100%)",  # Yellow
        "bananas": "linear-gradient(135deg, #ffe066 0%, #fcc419 100%)",
        "orange": "linear-gradient(135deg, #ff922b 0%, #fd7e14 100%)",  # Orange
        "oranges": "linear-gradient(135deg, #ff922b 0%, #fd7e14 100%)",
        "grape": "linear-gradient(135deg, #9775fa 0%, #7950f2 100%)",  # Purple
        "grapes": "linear-gradient(135deg, #9775fa 0%, #7950f2 100%)",
        "strawberry": "linear-gradient(135deg, #ff6b9d 0%, #f06595 100%)",  # Pink
        "strawberries": "linear-gradient(135deg, #ff6b9d 0%, #f06595 100%)",
        "watermelon": "linear-gradient(135deg, #20c997 0%, #12b886 100%)",  # Green
        
        # Electronics
        "laptop": "linear-gradient(135deg, #495057 0%, #212529 100%)",  # Dark Gray
        "laptops": "linear-gradient(135deg, #495057 0%, #212529 100%)",
        "phone": "linear-gradient(135deg, #4dabf7 0%, #228be6 100%)",  # Blue
        "phones": "linear-gradient(135deg, #4dabf7 0%, #228be6 100%)",
        "tablet": "linear-gradient(135deg, #74c0fc 0%, #4c6ef5 100%)",  # Light Blue
        "tablets": "linear-gradient(135deg, #74c0fc 0%, #4c6ef5 100%)",
        "headphone": "linear-gradient(135deg, #343a40 0%, #1a1e21 100%)",  # Black
        "headphones": "linear-gradient(135deg, #343a40 0%, #1a1e21 100%)",
        "keyboard": "linear-gradient(135deg, #868e96 0%, #495057 100%)",  # Gray
        "mouse": "linear-gradient(135deg, #ced4da 0%, #adb5bd 100%)",  # Light Gray
        
        # Vegetables
        "tomato": "linear-gradient(135deg, #ff6b6b 0%, #fa5252 100%)",  # Red
        "tomatoes": "linear-gradient(135deg, #ff6b6b 0%, #fa5252 100%)",
        "carrot": "linear-gradient(135deg, #ff922b 0%, #fd7e14 100%)",  # Orange
        "carrots": "linear-gradient(135deg, #ff922b 0%, #fd7e14 100%)",
        "broccoli": "linear-gradient(135deg, #51cf66 0%, #37b24d 100%)",  # Green
        "potato": "linear-gradient(135deg, #a9907e 0%, #8d6e63 100%)",  # Brown
        "onion": "linear-gradient(135deg, #f4e4ba 0%, #ddb892 100%)",  # Beige
        "cucumber": "linear-gradient(135deg, #51cf66 0%, #2f9e44 100%)",  # Green
        
        # Clothing
        "shirt": "linear-gradient(135deg, #748ffc 0%, #5c7cfa 100%)",  # Blue
        "t-shirt": "linear-gradient(135deg, #748ffc 0%, #5c7cfa 100%)",
        "pants": "linear-gradient(135deg, #4c6ef5 0%, #364fc7 100%)",  # Dark Blue
        "jeans": "linear-gradient(135deg, #3b5bdb 0%, #364fc7 100%)",
        "shoes": "linear-gradient(135deg, #845ef7 0%, #7048e8 100%)",  # Purple
        "sneakers": "linear-gradient(135deg, #845ef7 0%, #7048e8 100%)",
        "jacket": "linear-gradient(135deg, #343a40 0%, #1a1e21 100%)",  # Dark
        "dress": "linear-gradient(135deg, #ff6b9d 0%, #f06595 100%)",  # Pink
        "sweater": "linear-gradient(135deg, #91a7ff 0%, #748ffc 100%)",
        "shorts": "linear-gradient(135deg, #74c0fc 0%, #4dabf7 100%)",
        "boots": "linear-gradient(135deg, #5f3e31 0%, #3e2723 100%)",  # Brown
        "sandals": "linear-gradient(135deg, #f59f00 0%, #f08c00 100%)",
        
        # Mobiles & Electronics
        "iphone": "linear-gradient(135deg, #e9ecef 0%, #adb5bd 100%)",  # Silver
        "iphone 15": "linear-gradient(135deg, #e9ecef 0%, #adb5bd 100%)",
        "iphone 15 pro": "linear-gradient(135deg, #495057 0%, #343a40 100%)",  # Titanium
        "samsung": "linear-gradient(135deg, #4dabf7 0%, #228be6 100%)",  # Blue
        "samsung galaxy": "linear-gradient(135deg, #4dabf7 0%, #228be6 100%)",
        "samsung galaxy s24": "linear-gradient(135deg, #845ef7 0%, #7950f2 100%)",
        "google pixel": "linear-gradient(135deg, #51cf66 0%, #37b24d 100%)",  # Green
        "google pixel 8": "linear-gradient(135deg, #ff6b6b 0%, #fa5252 100%)",  # Coral
        "oneplus": "linear-gradient(135deg, #ff6b6b 0%, #f03e3e 100%)",  # Red
        "oneplus 12": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "xiaomi": "linear-gradient(135deg, #ff922b 0%, #fd7e14 100%)",  # Orange
        "xiaomi 14": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        
        # Laptops
        "macbook": "linear-gradient(135deg, #ced4da 0%, #adb5bd 100%)",  # Silver
        "macbook pro": "linear-gradient(135deg, #495057 0%, #343a40 100%)",
        "macbook pro m3": "linear-gradient(135deg, #212529 0%, #000000 100%)",
        "dell": "linear-gradient(135deg, #4dabf7 0%, #339af0 100%)",  # Blue
        "dell xps": "linear-gradient(135deg, #ced4da 0%, #adb5bd 100%)",
        "dell xps 15": "linear-gradient(135deg, #495057 0%, #343a40 100%)",
        "hp": "linear-gradient(135deg, #4c6ef5 0%, #4263eb 100%)",  # HP Blue
        "hp spectre": "linear-gradient(135deg, #212529 0%, #000000 100%)",
        "lenovo": "linear-gradient(135deg, #ff6b6b 0%, #f03e3e 100%)",  # Red
        "lenovo thinkpad": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "asus": "linear-gradient(135deg, #ffd43b 0%, #fab005 100%)",  # Gold
        "asus rog": "linear-gradient(135deg, #ff6b6b 0%, #f03e3e 100%)",
        
        # Watches
        "watch": "linear-gradient(135deg, #868e96 0%, #495057 100%)",
        "apple watch": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "apple watch series 9": "linear-gradient(135deg, #495057 0%, #343a40 100%)",
        "samsung galaxy watch": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "garmin": "linear-gradient(135deg, #4dabf7 0%, #228be6 100%)",
        "garmin fenix": "linear-gradient(135deg, #495057 0%, #343a40 100%)",
        "fitbit": "linear-gradient(135deg, #51cf66 0%, #37b24d 100%)",
        
        # Headphones & Audio
        "airpods": "linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)",
        "airpods pro": "linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)",
        "sony": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "sony wh-1000xm5": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "bose": "linear-gradient(135deg, #495057 0%, #343a40 100%)",
        "bose qc45": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "samsung buds": "linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)",
        
        # Cameras
        "camera": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "canon": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "canon eos": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "sony a7": "linear-gradient(135deg, #343a40 0%, #212529 100%)",
        "nikon": "linear-gradient(135deg, #ffd43b 0%, #f59f00 100%)",  # Yellow
        "fujifilm": "linear-gradient(135deg, #495057 0%, #343a40 100%)",
        
        # Food
        "pizza": "linear-gradient(135deg, #ffd43b 0%, #fab005 100%)",
        "burger": "linear-gradient(135deg, #f59f00 0%, #e67700 100%)",
        "pasta": "linear-gradient(135deg, #ffe066 0%, #fcc419 100%)",
        "rice": "linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%)",
        "noodles": "linear-gradient(135deg, #ffe066 0%, #fcc419 100%)",
        "sandwich": "linear-gradient(135deg, #a9907e 0%, #8d6e63 100%)",
        }
        
        # Get color based on product name (case-insensitive)
        product_lower = name.lower()
        gradient = color_map.get(product_lower, "linear-gradient(135deg, #667eea 0%, #764ba2 100%)")  # Default purple
    
    return Div(
        Div(
            H4(name, cls="product-name"),
            Div(
                Span(f"Quantity: {quantity}", cls="product-qty"),
                cls="product-details"
            ),
            cls="product-info"
        ),
        cls="product-card",
        style=f"background: {gradient};"
    )
