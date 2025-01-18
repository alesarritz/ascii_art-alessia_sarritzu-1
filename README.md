# ASCII Art Generator

## Overview
The Artistic ASCII Art Generator is a Python program that transforms user-provided text into beautiful ASCII art using various artistic fonts. Each generated piece of art is displayed in a randomly selected font for added creativity.

## Features
- Converts simple text into ASCII art.
- Supports a wide variety of artistic fonts.
- Displays the font name used for each generated artwork.
- Simple and user-friendly command-line interface.

## Requirements
- Python 3.x
- The `pyfiglet` library

## Installation
1. Clone this repository or download the script file.
2. Install the required library using pip:
   ```bash
   pip install pyfiglet
   ```

## Usage
1. Run the script:
   ```bash
   python ascii_art_generator.py
   ```
2. Enter the text you want to transform into ASCII art.
3. The program will display the generated ASCII art and the font name used.
4. To exit the program, type `exit`.

## Example
```plaintext
Welcome to the Artistic ASCII Art Generator!

Enter text to generate ASCII art (or type 'exit' to quit): Hello

Using font: slant

   _   _      _ _         __        __         _     _
  | | | | ___| | | ___    \ \      / /__  _ __| | __| |
  | |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` |
  |  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |
  |_| |_|\___|_|_|\___( )    \_/\_/ \___/|_|  |_|\__,_|
                     |/                                 

Enter text to generate ASCII art (or type 'exit' to quit): exit
Goodbye! Stay artistic!
```

## License
This project is open-source and available under the MIT License.

