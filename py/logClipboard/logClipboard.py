import pyperclip
import time


def main():
    # Specify the output file name
    output_file = "clipboard_log.txt"

    # Initialize the clipboard contents
    clipboard_contents = pyperclip.paste()
    while True:
        # Get the current clipboard contents
        new_contents = pyperclip.paste()

        # If the clipboard has changed, write the new contents to the output file
        if new_contents != clipboard_contents:
            with open(output_file, "a") as f:
                print("Writing to file: " + new_contents)
                f.write(new_contents + "\n")

            # Update the clipboard contents
            clipboard_contents = new_contents

        # Wait for a short time before checking the clipboard again
        time.sleep(0.1)


if __name__ == '__main__':
    main()
