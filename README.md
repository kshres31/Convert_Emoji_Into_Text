# Emoji Text Converter

Emoji Text Converter is a small command-line Python project for exploring Unicode text. It can find emojis in a message, remove them, replace them with descriptive names, and count how often each emoji appears.

## Features

- Detect emojis and display their descriptions
- Remove emojis without changing the rest of the message
- Replace emojis with readable `:descriptions:`
- Show total and per-emoji statistics
- Process as many messages as needed during one run
- Handle empty input and invalid menu choices without crashing

## Technologies

- Python 3
- [demoji](https://pypi.org/project/demoji/) for emoji recognition and descriptions
- `unittest` from the Python standard library
- Git

## Installation

Create and activate a virtual environment from the project directory:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

`demoji` includes the emoji data needed by the program, so processing text does not require an internet connection after installation.

## Usage

Run the application from the project directory:

```bash
python main.py
```

Choose an option from the menu, enter a message, and then choose another action. Select `5` to exit.

Example:

```text
Choose an option: 3

Enter text: I love Python 🐍 and coding 💻🔥

Converted:
I love Python :snake: and coding :laptop::fire:
```

Option `1` lists each emoji and its description. Option `4` reports the total and counts repeated emojis.

## Project Structure

```text
├── src/
│   ├── converter.py       # Reusable conversion and counting functions
│   ├── main.py            # Interactive menu
│   └── statistics.py      # Statistics report formatting
├── tests/
│   └── test_converter.py  # Unit tests for conversion behavior
├── examples/
│   └── example_text.txt   # Sample input
├── main.py                # Root command-line entry point
├── requirements.txt       # External dependency list
└── .gitignore
```

## Running Tests

No test framework installation is required:

```bash
python -m unittest discover -s tests -v
```

## What I Learned

This project gave me practice working with an external Python package, Unicode strings, dictionaries and `Counter`, reusable functions, input validation, a looping CLI menu, and unit testing. Separating the converter logic from the menu also makes the useful parts easier to test without simulating every prompt.

## Possible Improvements

A future version could support reading a text file, exporting converted text, choosing between several replacement styles, or adding a small graphical interface.
