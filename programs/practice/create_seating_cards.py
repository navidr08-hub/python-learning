# from PIL import Image, ImageDraw, ImageFont
# import os

# # === CONFIG ===
# CARD_WIDTH = 360   # 5 inches × 72 dpi
# CARD_HEIGHT = 288  # 4 inches × 72 dpi
# FONT_PATH = "arial.ttf"  # Replace with a local TTF file path
# FONT_SIZE = 24
# OUTPUT_DIR = "seating_cards"
# FLOWER_IMAGE = "flower.png"  # Optional decorative image

# def create_card(name):
#     """Generate a seating card image for a single guest."""
#     # Create blank white card
#     card = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), "white")
#     draw = ImageDraw.Draw(card)

#     # Draw black border
#     border_thickness = 5
#     draw.rectangle(
#         [(border_thickness, border_thickness),
#          (CARD_WIDTH - border_thickness, CARD_HEIGHT - border_thickness)],
#         outline="black", width=3
#     )

#     # Optional: add flower decoration
#     if os.path.exists(FLOWER_IMAGE):
#         flower = Image.open(FLOWER_IMAGE).convert("RGBA")
#         flower = flower.resize((80, 80))  # Adjust size as needed
#         card.paste(flower, (10, 10), flower)  # top-left corner

#     # Add guest name (centered)
#     try:
#         font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
#     except IOError:
#         font = ImageFont.load_default()

#     text_w, text_h = draw.textsize(name, font=font)
#     text_x = (CARD_WIDTH - text_w) / 2
#     text_y = (CARD_HEIGHT - text_h) / 2

#     draw.text((text_x, text_y), name, font=font, fill="black")

#     # Save output
#     os.makedirs(OUTPUT_DIR, exist_ok=True)
#     card.save(os.path.join(OUTPUT_DIR, f"{name.replace(' ', '_')}.png"))

# def create_cards(guests_file):
#     with open(guests_file, "r") as f:
#         guests = [line.strip() for line in f if line.strip()]

#     for guest in guests:
#         print(f"Creating card for {guest}...")
#         create_card(guest)

#     print(f"✅ Done! Cards saved in '{OUTPUT_DIR}/'")

# if __name__ == "__main__":
#     create_cards("guests.txt")


import os
import sys
from PIL import Image, ImageDraw, ImageFont

BACKGROUND_IMG = ".\\static\\flower_card.jpg"
CARD_WIDTH = 600
CARD_HEIGHT = 400
FONT_SIZE = 32
FONT_PATH = "C:\\Users\\navid\\Documents\\fonts\\Playwrite_DE_SAS\\static\\PlaywriteDESAS-Regular.ttf"
SEATING_DIR = "C:\\Users\\navid\\Documents\\programs\\seating-cards"
GUESTS_FILE = "C:\\Users\\navid\\Documents\\programs\\static\\guests.txt"


def get_guests(guests_file: str):
    try:
        with open(guests_file, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]

        return lines
    except FileNotFoundError:
        print(f"Guest file {guests_file} not found")
        sys.exit(1)


def create_seating_card(guest: str, seat_num: int):
    im = Image.open(BACKGROUND_IMG).convert("RGBA")
    draw = ImageDraw.Draw(im)

    # Draw black border
    draw.rectangle(
        [(0, 0), (CARD_WIDTH, CARD_HEIGHT)],
        outline="black", width=10
    )

    # Add guest name (centered)
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except IOError:
        font = ImageFont.load_default()

    text_w, text_h = draw.textsize(guest, font=font)
    text_x = (CARD_WIDTH - text_w) / 2
    text_y = (CARD_HEIGHT - (2 * text_h)) / 2
    draw.text((text_x, text_y), guest, font=font, fill="black")

    text_w, text_h = draw.textsize(f"Seat: {seat_num}", font=font)
    text_x = (CARD_WIDTH - text_w) / 2
    text_y = (text_y + (1.5 * text_h))
    draw.text((text_x, text_y), f"Seat: {seat_num}", font=font, fill="black")

    return im


def create_seating_cards(guests_file: str):
    guests = get_guests(guests_file)
    for seat_num, guest in enumerate(guests):
        card = create_seating_card(guest, seat_num)
        card.show()
    

def main():
    create_seating_cards(GUESTS_FILE)


if __name__ == "__main__":
    main()