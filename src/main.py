"""Command-line interface for the Emoji Text Converter."""

from .converter import detect_emojis, get_emoji_statistics, remove_emojis, replace_emojis
from .statistics import format_statistics


def display_menu() -> None:
    """Print the available actions."""
    print("\n================================")
    print("       EMOJI TEXT CONVERTER")
    print("================================")
    print("1. Detect emojis")
    print("2. Remove emojis")
    print("3. Replace emojis with text")
    print("4. Show emoji statistics")
    print("5. Exit")


def get_text() -> str | None:
    """Read text from the user, rejecting empty input."""
    text = input("\nEnter text: ").strip()
    if not text:
        print("Please enter some text.")
        return None
    return text


def show_detected(text: str) -> None:
    matches = detect_emojis(text)
    if not matches:
        print("No emojis found.")
        return
    print("\nDetected emojis:")
    for emoji, description in matches:
        print(f"{emoji} -> {description}")


def main() -> None:
    """Run the menu until the user chooses to exit."""
    while True:
        display_menu()
        choice = input("\nChoose an option: ").strip()
        if choice == "5":
            print("Thanks for using Emoji Text Converter!")
            return
        if choice not in {"1", "2", "3", "4"}:
            print("Invalid option. Please choose between 1 and 5.")
            continue

        text = get_text()
        if text is None:
            continue
        if choice == "1":
            show_detected(text)
        elif choice == "2":
            print(f"\nConverted:\n{remove_emojis(text)}")
        elif choice == "3":
            print(f"\nConverted:\n{replace_emojis(text)}")
        else:
            matches = dict(detect_emojis(text))
            print(format_statistics(get_emoji_statistics(text), matches))


if __name__ == "__main__":
    main()
