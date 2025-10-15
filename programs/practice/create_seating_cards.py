# Chapter 21 - Graphs and Manipulating Images
# (Practice Program) - Create Custom Seating Cards

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
    guests = get_guests(GUESTS_FILE)
    for seat_num, guest in enumerate(guests):
        card = create_seating_card(guest, seat_num)
        card.show()
    

def main():
    create_seating_cards(GUESTS_FILE)


if __name__ == "__main__":
    main()