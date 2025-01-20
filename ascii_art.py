import pyfiglet
import random
import argparse

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
            if selected_font not in fonts:
                raise KeyError(f"Font '{selected_font}' is not available.")
            
            ascii_art = pyfiglet.figlet_format(user_input, font=selected_font)
            print(f"\nUsing font: {selected_font}\n")
            print(ascii_art)
        except KeyError as e:
            print(f"An error occurred: {e}. Selecting default font.")
            default_font = "slant"
            ascii_art = pyfiglet.figlet_format(user_input, font=default_font)
            print(f"\nUsing default font: {default_font}\n")
            print(ascii_art)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def ascii_art_generator_cli():
    parser = argparse.ArgumentParser(description="Generate ASCII art from text.")
    parser.add_argument("text", type=str, help="The text to convert into ASCII art.")
    parser.add_argument("--font", type=str, help="The font to use for ASCII art.")

    args = parser.parse_args()

    try:
        fonts = pyfiglet.FigletFont.getFonts()
        selected_font = args.font if args.font else random.choice(fonts)

        if selected_font not in fonts:
            raise KeyError(f"Font '{selected_font}' is not available. Using default font.")

        ascii_art = pyfiglet.figlet_format(args.text, font=selected_font)
        print(f"\nUsing font: {selected_font}\n")
        print(ascii_art)
    except KeyError as e:
        print(f"An error occurred: {e}")
        default_font = "slant"
        ascii_art = pyfiglet.figlet_format(args.text, font=default_font)
        print(f"\nUsing default font: {default_font}\n")
        print(ascii_art)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # ascii_art_generator_cli() # use CLI instead of interactive mode
    ascii_art_generator()