# TelegramTextBot

TelegramTextBot is a Python script designed for automating the sending of amusing messages on Telegram. It simplifies the process of sending predefined sentences from a text file to create entertaining conversations.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/TelegramTextBot.git
   cd TelegramTextBot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a text file (`textfile.txt`) containing the sentences you want to send, with each sentence on a new line.

4. Run the script:

   ```bash
   python TelegramTextBot.py
   ```

   The script will wait for a few seconds before starting to input text. It will then read sentences from the text file, copy them to the clipboard, and send them to the Telegram chat with a delay between each message.

## Configuration

You can customize the script by modifying the parameters inside the `send_sentences_from_file` function in `TelegramTextBot.py`. For example, you can adjust the delay between messages.

```python
# Set the path to your text file
file_path = 'textfile.txt'

# Adjust the delay between messages (in seconds)
time.sleep(1)
```

## Contributing

If you have any improvements or suggestions, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

```

Make sure to create a `LICENSE` file with the appropriate license text for your project, and include it in the same directory as your script. You can choose a license that suits your project's needs from [choosealicense.com](https://choosealicense.com/).
