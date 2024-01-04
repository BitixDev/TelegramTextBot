import time
import keyboard
import pyperclip

def send_sentences_from_file(file_path):
    while True:
        # Wait for a few seconds before starting to input text
        time.sleep(5)

        with open(file_path, 'r', encoding='utf-8') as file:
            sentences = file.readlines()

        for sentence in sentences:
            # Copy the sentence to the clipboard
            pyperclip.copy(sentence.strip())

            # Paste the text from the clipboard
            keyboard.press_and_release('ctrl+v')

            # Press the Enter key to send the message
            keyboard.press_and_release('enter')

            # Pause between sending messages (adjustable)
            time.sleep(1)

if __name__ == "__main__":
    file_path = 'textfile.txt'
    send_sentences_from_file(file_path)
