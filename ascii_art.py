import pyfiglet
import random


def ascii_art_generator():
    print("Welcome to the Artistic ASCII Art Generator!\n")
    fonts = pyfiglet.FigletFont.getFonts()

    while True:
        user_input = input("Enter text to generate ASCII art (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye! Stay artistic!")
            break

        try:
            selected_font = random.choice(fonts)
            ascii_art = pyfiglet.figlet_format(user_input, font=selected_font)
            print(f"\nUsing font: {selected_font}\n")
            print(ascii_art)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    ascii_art_generator()
