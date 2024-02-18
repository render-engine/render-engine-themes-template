import logging
import pathlib
import json

# Setup up logging to setup.log
logging.basicConfig(filename="setup.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


def replace_value(original_content: str, original_string: str, replacement: str) -> str:
    """
    Replace the original string with the replacement string in the original content
    """
    # replace all instances of the original string with the replacement string
    return original_content.replace(
        original_string,
        replacement,
    )


def replace_values_in_json():
    """
    Read in the values of "abbreviations.json" and replace them throughout the project
    """
    with open("abbreviations.json") as json_file:
        replacements = json.loads(json_file.read())

    for path in pathlib.Path("content").rglob("*"):
        if path.is_file():
            with open(path, "r") as file:
                file_contents = file.read()
        for item, value in replacements.items:
            file_contents = replace_value(file_contents, item, value)

        print("Done!")


if __name__ == "__main__":
    replace_values_in_json()
