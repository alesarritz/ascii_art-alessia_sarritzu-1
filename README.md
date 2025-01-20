# ASCII Art Generator

## Description
The Artistic ASCII Art Generator is a Python-based program that allows users to convert plain text into beautiful ASCII art. Each piece of art is created using a randomly selected artistic font, making every output unique and visually appealing. This program is ideal for adding creative flair to text or for exploring the artistic potential of ASCII.

## How to Run the Project
### Prerequisites
- Python 3.x installed on your system.
- The `pyfiglet` library installed (instructions below).

### Steps to Run
1. Clone this repository or download the `ascii_art_generator.py` script file.
2. Install the required library:
   ```bash
   pip install pyfiglet
   ```
3. Run the script:
   ```bash
   python ascii_art_generator.py
   ```
4. Enter the text you want to convert into ASCII art when prompted.
5. To exit the program, type `exit`.

### Example
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
## Contribution Guide

We welcome contributions to make the ASCII Art Generator even better! Here’s how you can contribute:

### 1. **Fork the Repository**
- Click the “Fork” button on the top-right corner of the repository page to create your copy.

### 2. **Clone Your Fork**
- Clone the forked repository to your local machine:
  ```bash
  git clone https://github.com/<your-username>/ascii-art-generator.git
  ```
  Replace `<your-username>` with your GitHub username.

### 3. **Set Up Your Environment**
- Ensure you have Python 3.x installed. You can check this by running:
  ```bash
  python --version
  ```
- [Optional] Set up a virtual environment to manage dependencies:
  ```bash
  python -m venv env
  source env/bin/activate  # On Windows, use `env\Scripts\activate`
  ```
- Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 4. **Create a New Branch**
- Create a branch for your feature or bug fix:
  ```bash
  git checkout -b feature-name
  ```

### 5. **Make Your Changes**
- Edit the code or documentation to add features or fix issues.

### 6. **Test Your Changes**
- Run the script to ensure your changes work correctly:
  ```bash
  python ascii_art_generator.py
  ```

### 7. **Commit and Push**
- Commit your changes with a meaningful message:
  ```bash
  git commit -m "Add new feature or fix bug"
  ```
- Push your changes to your fork:
  ```bash
  git push origin feature-name
  ```

### 8. **Submit a Pull Request**
- Go to the original repository and click “New Pull Request.”
- Describe your changes and submit the pull request for review.

### Additional Resources for Beginners
- [GitHub Docs](https://docs.github.com/en/get-started/quickstart) – Learn the basics of using Git and GitHub.
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html) – Understand how to create and use virtual environments.
- [Troubleshooting Pip Installation Issues](https://pip.pypa.io/en/stable/user_guide/#installing-packages) – Common solutions for `pip`-related problems.


## License
This project is open-source and available under the MIT License.

